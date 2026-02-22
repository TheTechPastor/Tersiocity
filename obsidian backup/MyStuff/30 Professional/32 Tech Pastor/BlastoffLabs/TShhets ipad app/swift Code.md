// QuickBooks Time (TSheets) iPad App – SwiftUI Scaffold
// Swift 5.9+ / iOS 17+
// Notes:
// - Uses OAuth 2.0 + PKCE (no client secret in-app)
// - ASWebAuthenticationSession for the login flow
// - Keychain for secure token storage
// - Simple API client + models + offline cache (in-memory) + minimal views
// - Replace placeholders in OAuthConfig with your real values
//
// =============================
// FILE: TSTimeApp.swift
// =============================
import SwiftUI

@main
struct TSTimeApp: App {
    @StateObject private var store = AppStore()

    var body: some Scene {
        WindowGroup {
            RootView()
                .environmentObject(store)
        }
    }
}

// =============================
// FILE: RootView.swift
// =============================
import SwiftUI

struct RootView: View {
    @EnvironmentObject var store: AppStore

    var body: some View {
        Group {
            if store.sessionState == .authenticated {
                DashboardView()
            } else {
                LoginView()
            }
        }
        .task {
            await store.bootstrap()
        }
        .alert(item: $store.appError) { e in
            Alert(title: Text("Error"), message: Text(e.message), dismissButton: .default(Text("OK")))
        }
    }
}

// =============================
// FILE: AppStore.swift
// =============================
import Foundation
import SwiftUI

@MainActor
final class AppStore: ObservableObject {
    enum SessionState { case unauthenticated, authenticated }

    @Published var sessionState: SessionState = .unauthenticated
    @Published var me: QBUser?
    @Published var jobcodes: [QBJobcode] = []
    @Published var todaysTimesheets: [QBTimesheet] = []
    @Published var appError: AppError?

    private let oauth = OAuthService()
    private let api = QBTimeAPI()

    func bootstrap() async {
        if await oauth.hasValidToken() {
            sessionState = .authenticated
            await refreshDictionaries()
            await refreshToday()
        } else {
            sessionState = .unauthenticated
        }
    }

    func signIn() async {
        do {
            try await oauth.signIn()
            sessionState = .authenticated
            await refreshDictionaries()
            await refreshToday()
        } catch {
            appError = AppError(message: error.localizedDescription)
        }
    }

    func signOut() async {
        await oauth.signOut()
        sessionState = .unauthenticated
        me = nil
        jobcodes.removeAll()
        todaysTimesheets.removeAll()
    }

    func refreshDictionaries() async {
        do {
            me = try await api.currentUser()
            jobcodes = try await api.jobcodes()
        } catch { appError = AppError(message: error.localizedDescription) }
    }

    func refreshToday() async {
        do {
            let (start, end) = Date.todayBounds()
            todaysTimesheets = try await api.timesheets(start: start, end: end)
        } catch { appError = AppError(message: error.localizedDescription) }
    }

    func clockIn(jobcode: QBJobcode, notes: String? = nil) async {
        do {
            let ts = try await api.clockIn(jobcodeId: jobcode.id, notes: notes)
            todaysTimesheets.insert(ts, at: 0)
        } catch { appError = AppError(message: error.localizedDescription) }
    }

    func clockOut() async {
        do {
            if let ts = try await api.clockOut() {
                if let idx = todaysTimesheets.firstIndex(where: { $0.id == ts.id }) {
                    todaysTimesheets[idx] = ts
                } else {
                    todaysTimesheets.insert(ts, at: 0)
                }
            }
        } catch { appError = AppError(message: error.localizedDescription) }
    }
}

struct AppError: Identifiable { let id = UUID(); let message: String }

// =============================
// FILE: OAuthService.swift
// =============================
import Foundation
import AuthenticationServices
import CryptoKit

actor OAuthService {
    private let cfg = OAuthConfig()
    private let keychain = TokenStore()

    func hasValidToken() async -> Bool {
        guard let token = keychain.read() else { return false }
        if token.isExpired, let _ = await refreshTokenIfNeeded() { return true }
        return !token.isExpired
    }

    func signIn() async throws {
        let pkce = PKCE()
        let url = cfg.authorizationURL(codeChallenge: pkce.codeChallenge)
        let callbackURL = try await ASWebAuth.start(url: url, callbackScheme: cfg.redirectScheme)
        let code = try cfg.extractAuthorizationCode(from: callbackURL)
        let token = try await exchangeCodeForToken(code: code, verifier: pkce.codeVerifier)
        keychain.save(token)
    }

    func signOut() async {
        keychain.delete()
    }

    func withValidAccessToken() async throws -> String {
        if let token = keychain.read(), !token.isExpired { return token.accessToken }
        if let newToken = await refreshTokenIfNeeded() { return newToken.accessToken }
        throw NSError(domain: "auth", code: 401, userInfo: [NSLocalizedDescriptionKey: "Not signed in"])
    }

    private func refreshTokenIfNeeded() async -> OAuthToken? {
        guard let token = keychain.read(), token.refreshToken != nil else { return nil }
        do {
            let newToken = try await refresh(token: token)
            keychain.save(newToken)
            return newToken
        } catch { return nil }
    }

    private func exchangeCodeForToken(code: String, verifier: String) async throws -> OAuthToken {
        var req = URLRequest(url: cfg.tokenURL)
        req.httpMethod = "POST"
        req.setValue("application/x-www-form-urlencoded", forHTTPHeaderField: "Content-Type")

        let body = [
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": cfg.redirectURI,
            "client_id": cfg.clientId,
            "code_verifier": verifier
        ]
        req.httpBody = body.formURLEncoded().data(using: .utf8)

        let (data, resp) = try await URLSession.shared.data(for: req)
        try resp.ensureHTTP200()
        return try JSONDecoder().decode(OAuthToken.self, from: data)
    }

    private func refresh(token: OAuthToken) async throws -> OAuthToken {
        guard let refresh = token.refreshToken else { throw NSError(domain: "auth", code: 401, userInfo: [NSLocalizedDescriptionKey: "Missing refresh token"]) }
        var req = URLRequest(url: cfg.tokenURL)
        req.httpMethod = "POST"
        req.setValue("application/x-www-form-urlencoded", forHTTPHeaderField: "Content-Type")
        let body = [
            "grant_type": "refresh_token",
            "refresh_token": refresh,
            "client_id": cfg.clientId
        ]
        req.httpBody = body.formURLEncoded().data(using: .utf8)

        let (data, resp) = try await URLSession.shared.data(for: req)
        try resp.ensureHTTP200()
        return try JSONDecoder().decode(OAuthToken.self, from: data)
    }
}

// =============================
// FILE: OAuthSupport.swift
// =============================
import Foundation
import AuthenticationServices
import CryptoKit

struct OAuthConfig {
    // TODO: Replace these placeholders
    let clientId = "YOUR_QB_TIME_CLIENT_ID"
    let redirectScheme = "yourapp"            // e.g., yourapp://oauth-callback
    let redirectHost = "oauth-callback"
    let authBase = URL(string: "https://app.tsheets.com")! // confirm with your env
    let tokenBase = URL(string: "https://rest.tsheets.com")!

    var redirectURI: String { "\(redirectScheme)://\(redirectHost)" }

    // Scopes: adjust to least privilege for your app
    let scopes = ["user", "timesheets", "jobcodes", "manage_timesheets"]

    var tokenURL: URL { tokenBase.appending(path: "/oauth2/token") }

    func authorizationURL(codeChallenge: String) -> URL {
        var comps = URLComponents(url: authBase.appending(path: "/oauth2/authorize"), resolvingAgainstBaseURL: false)!
        comps.queryItems = [
            .init(name: "client_id", value: clientId),
            .init(name: "response_type", value: "code"),
            .init(name: "redirect_uri", value: redirectURI),
            .init(name: "scope", value: scopes.joined(separator: ",")),
            .init(name: "code_challenge", value: codeChallenge),
            .init(name: "code_challenge_method", value: "S256")
        ]
        return comps.url!
    }

    func extractAuthorizationCode(from callbackURL: URL) throws -> String {
        guard callbackURL.scheme == redirectScheme, callbackURL.host == redirectHost else {
            throw NSError(domain: "oauth", code: 0, userInfo: [NSLocalizedDescriptionKey: "Invalid redirect URL"])
        }
        let comps = URLComponents(url: callbackURL, resolvingAgainstBaseURL: false)
        let code = comps?.queryItems?.first(where: { $0.name == "code" })?.value
        if let code { return code }
        throw NSError(domain: "oauth", code: 0, userInfo: [NSLocalizedDescriptionKey: "Authorization code missing"])
    }
}

struct PKCE {
    let codeVerifier: String
    let codeChallenge: String

    init() {
        self.codeVerifier = PKCE.randomURLSafeString(length: 64)
        self.codeChallenge = PKCE.sha256base64url(codeVerifier)
    }

    private static func randomURLSafeString(length: Int) -> String {
        let chars = Array("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-._~")
        return String((0..<length).map { _ in chars.randomElement()! })
    }

    private static func sha256base64url(_ s: String) -> String {
        let data = Data(s.utf8)
        let digest = SHA256.hash(data: data)
        return Data(digest).base64EncodedString()
            .replacingOccurrences(of: "+", with: "-")
            .replacingOccurrences(of: "/", with: "_")
            .replacingOccurrences(of: "=", with: "")
    }
}

enum ASWebAuth {
    static func start(url: URL, callbackScheme: String) async throws -> URL {
        try await withCheckedThrowingContinuation { cont in
            let session = ASWebAuthenticationSession(url: url, callbackURLScheme: callbackScheme) { callbackURL, error in
                if let error { cont.resume(throwing: error) }
                else if let callbackURL { cont.resume(returning: callbackURL) }
                else { cont.resume(throwing: URLError(.badServerResponse)) }
            }
            session.prefersEphemeralWebBrowserSession = true
            session.start()
        }
    }
}

extension Dictionary where Key == String, Value == String {
    func formURLEncoded() -> String {
        map { key, value in
            let k = key.addingPercentEncoding(withAllowedCharacters: .urlQueryAllowed) ?? key
            let v = value.addingPercentEncoding(withAllowedCharacters: .urlQueryAllowed) ?? value
            return "\(k)=\(v)"
        }.joined(separator: "&")
    }
}

extension URLResponse {
    func ensureHTTP200() throws {
        guard let http = self as? HTTPURLResponse else { return }
        guard (200..<300).contains(http.statusCode) else {
            throw NSError(domain: "http", code: http.statusCode, userInfo: [NSLocalizedDescriptionKey: "HTTP \(http.statusCode)"])
        }
    }
}

// =============================
// FILE: TokenStore.swift
// =============================
import Foundation
import Security

struct OAuthToken: Codable {
    let accessToken: String
    let refreshToken: String?
    let expiresIn: TimeInterval
    let tokenType: String
    let createdAt: Date

    enum CodingKeys: String, CodingKey {
        case accessToken = "access_token"
        case refreshToken = "refresh_token"
        case expiresIn = "expires_in"
        case tokenType = "token_type"
        case createdAt = "created_at"
    }

    var isExpired: Bool { Date().timeIntervalSince(createdAt) > (expiresIn - 60) }
}

final class TokenStore {
    private let service = "com.example.tsheets"
    private let account = "oauth-token"

    func save(_ token: OAuthToken) {
        let data = try! JSONEncoder().encode(token)
        let query: [String: Any] = [kSecClass as String: kSecClassGenericPassword,
                                    kSecAttrService as String: service,
                                    kSecAttrAccount as String: account]
        SecItemDelete(query as CFDictionary)
        var add: [String: Any] = query
        add[kSecValueData as String] = data
        SecItemAdd(add as CFDictionary, nil)
    }

    func read() -> OAuthToken? {
        let query: [String: Any] = [kSecClass as String: kSecClassGenericPassword,
                                    kSecAttrService as String: service,
                                    kSecAttrAccount as String: account,
                                    kSecReturnData as String: true,
                                    kSecMatchLimit as String: kSecMatchLimitOne]
        var out: CFTypeRef?
        let status = SecItemCopyMatching(query as CFDictionary, &out)
        guard status == errSecSuccess, let data = out as? Data else { return nil }
        return try? JSONDecoder().decode(OAuthToken.self, from: data)
    }

    func delete() { SecItemDelete([kSecClass as String: kSecClassGenericPassword, kSecAttrService as String: service, kSecAttrAccount as String: account] as CFDictionary) }
}

// =============================
// FILE: QBTimeAPI.swift
// =============================
import Foundation

struct QBUser: Identifiable, Codable { let id: Int; let name: String }
struct QBJobcode: Identifiable, Codable { let id: Int; let name: String; let active: Bool }
struct QBTimesheet: Identifiable, Codable {
    let id: Int
    let userId: Int
    let jobcodeId: Int
    var start: Date
    var end: Date?
    var notes: String?
}

actor QBTimeAPI {
    // Replace with the official base URL you target (prod/sandbox)
    private let base = URL(string: "https://rest.tsheets.com/api/v1")!
    private let oauth = OAuthService()

    private func authedRequest(_ path: String, method: String = "GET", body: Data? = nil, query: [URLQueryItem] = []) async throws -> (Data, HTTPURLResponse) {
        let token = try await oauth.withValidAccessToken()
        var comps = URLComponents(url: base.appending(path: path), resolvingAgainstBaseURL: false)!
        if !query.isEmpty { comps.queryItems = query }
        var req = URLRequest(url: comps.url!)
        req.httpMethod = method
        req.setValue("Bearer \(token)", forHTTPHeaderField: "Authorization")
        if let body { req.httpBody = body; req.setValue("application/json", forHTTPHeaderField: "Content-Type") }
        let (data, resp) = try await URLSession.shared.data(for: req)
        guard let http = resp as? HTTPURLResponse else { throw URLError(.badServerResponse) }
        if http.statusCode == 429 { throw NSError(domain: "rate", code: 429, userInfo: [NSLocalizedDescriptionKey: "Rate limited"]) }
        if !(200..<300).contains(http.statusCode) {
            let text = String(data: data, encoding: .utf8) ?? ""
            throw NSError(domain: "http", code: http.statusCode, userInfo: [NSLocalizedDescriptionKey: "HTTP \(http.statusCode) — \(text)"])
        }
        return (data, http)
    }

    // Current user
    func currentUser() async throws -> QBUser {
        let (data, _) = try await authedRequest("/current_user")
        return try JSONDecoder.tsheets.decode(QBUser.self, from: data)
    }

    // Jobcodes
    func jobcodes() async throws -> [QBJobcode] {
        let (data, _) = try await authedRequest("/jobcodes")
        return try JSONDecoder.tsheets.decode([QBJobcode].self, from: data)
    }

    // Timesheets (GET)
    func timesheets(start: Date, end: Date) async throws -> [QBTimesheet] {
        let fmt = ISO8601DateFormatter()
        let q = [URLQueryItem(name: "start_date", value: fmt.string(from: start)),
                 URLQueryItem(name: "end_date", value: fmt.string(from: end))]
        let (data, _) = try await authedRequest("/timesheets", query: q)
        return try JSONDecoder.tsheets.decode([QBTimesheet].self, from: data)
    }

    // Clock In (create running timesheet)
    func clockIn(jobcodeId: Int, notes: String?) async throws -> QBTimesheet {
        let payload: [String: Any] = [
            "jobcode_id": jobcodeId,
            "type": "regular",
            "notes": notes as Any?
        ].compactMapValues { $0 }
        let body = try JSONSerialization.data(withJSONObject: payload)
        let (data, _) = try await authedRequest("/timesheets", method: "POST", body: body)
        return try JSONDecoder.tsheets.decode(QBTimesheet.self, from: data)
    }

    // Clock Out (stop the currently running timesheet)
    func clockOut() async throws -> QBTimesheet? {
        // Implementation depends on your server model; a common approach is to PATCH the open timesheet with an end time = now
        // Here we fetch open sheets and close the first one.
        let open = try await timesheets(start: Date.distantPast, end: Date())
            .filter { $0.end == nil }
        guard let running = open.first else { return nil }
        let payload: [String: Any] = ["end": ISO8601DateFormatter().string(from: Date())]
        let body = try JSONSerialization.data(withJSONObject: payload)
        let (data, _) = try await authedRequest("/timesheets/\(running.id)", method: "PATCH", body: body)
        return try JSONDecoder.tsheets.decode(QBTimesheet.self, from: data)
    }
}

extension JSONDecoder {
    static var tsheets: JSONDecoder {
        let dec = JSONDecoder()
        dec.dateDecodingStrategy = .iso8601
        return dec
    }
}

// =============================
// FILE: Views.swift
// =============================
import SwiftUI

struct LoginView: View {
    @EnvironmentObject var store: AppStore
    @State private var isLoading = false

    var body: some View {
        VStack(spacing: 24) {
            Text("QuickBooks Time")
                .font(.largeTitle).bold()
            Text("Track time fast. Secure sign-in with Intuit.")
                .foregroundStyle(.secondary)

            Button {
                isLoading = true
                Task { await store.signIn(); isLoading = false }
            } label: {
                HStack { if isLoading { ProgressView() }; Text("Sign in with Intuit") }
            }
            .buttonStyle(.borderedProminent)
            .disabled(isLoading)
        }
        .padding()
    }
}

struct DashboardView: View {
    @EnvironmentObject var store: AppStore
    @State private var selectedJobcode: QBJobcode?
    @State private var note: String = ""

    var body: some View {
        NavigationStack {
            List {
                Section("Me") {
                    Text(store.me?.name ?? "—")
                }

                Section("Clock") {
                    Picker("Jobcode", selection: $selectedJobcode) {
                        ForEach(store.jobcodes) { jc in Text(jc.name).tag(Optional(jc)) }
                    }
                    .pickerStyle(.menu)

                    TextField("Note (optional)", text: $note)

                    HStack {
                        Button("Clock In") {
                            guard let jc = selectedJobcode else { return }
                            Task { await store.clockIn(jobcode: jc, notes: note.isEmpty ? nil : note) }
                        }
                        .buttonStyle(.borderedProminent)

                        Button("Clock Out") {
                            Task { await store.clockOut() }
                        }
                        .buttonStyle(.bordered)
                    }
                }

                Section("Today") {
                    ForEach(store.todaysTimesheets) { ts in
                        VStack(alignment: .leading, spacing: 4) {
                            Text(jobcodeName(id: ts.jobcodeId))
                                .font(.headline)
                            Text(timespanText(ts))
                                .font(.subheadline)
                                .foregroundStyle(.secondary)
                            if let n = ts.notes, !n.isEmpty { Text(n).font(.footnote) }
                        }
                    }
                }
            }
            .navigationTitle("Time Tracking")
            .toolbar {
                ToolbarItem(placement: .topBarTrailing) {
                    Menu {
                        Button("Refresh") { Task { await store.refreshToday() } }
                        Button("Sign Out", role: .destructive) { Task { await store.signOut() } }
                    } label: { Image(systemName: "ellipsis.circle") }
                }
            }
            .task { await store.refreshToday() }
        }
    }

    private func jobcodeName(id: Int) -> String {
        store.jobcodes.first(where: { $0.id == id })?.name ?? "Jobcode #\(id)"
    }

    private func timespanText(_ ts: QBTimesheet) -> String {
        let df = DateFormatter()
        df.timeStyle = .short
        if let end = ts.end { return "\(df.string(from: ts.start))–\(df.string(from: end))" }
        else { return "Started \(df.string(from: ts.start)) (running)" }
    }
}

// =============================
// FILE: Date+Helpers.swift
// =============================
import Foundation

extension Date {
    static func todayBounds() -> (Date, Date) {
        let cal = Calendar.current
        let start = cal.startOfDay(for: Date())
        let end = cal.date(byAdding: .day, value: 1, to: start)!
        return (start, end)
    }
}

// =============================
// FILE: InfoPlistNotes.txt
// =============================
/*
Add to Info.plist:

1) URL Types so your app can receive the OAuth redirect:

<key>CFBundleURLTypes</key>
<array>
  <dict>
    <key>CFBundleURLSchemes</key>
    <array>
      <string>yourapp</string> <!-- replace with OAuthConfig.redirectScheme -->
    </array>
  </dict>
</array>

2) NSAppTransportSecurity if your auth/env needs it (prefer HTTPS everywhere).

3) Optional: LSApplicationQueriesSchemes if you ever deep-link to Intuit apps.
*/

// =============================
// FILE: README_Scaffold.md
// =============================
/*
Quick start
-----------
1) Create an Intuit Developer app for QuickBooks Time. Configure your redirect URI exactly as: yourapp://oauth-callback
2) In OAuthConfig, set `clientId`, `redirectScheme`, `redirectHost`, and confirm auth/token base URLs for your environment.
3) Build & run on an iPad/iPad Simulator (iOS 17+). Tap "Sign in with Intuit" and complete the flow.
4) After sign-in, test: pick a jobcode → Clock In → Clock Out → Refresh Today.

Production to-dos
-----------------
- Replace the placeholder API paths with the authoritative QuickBooks Time endpoints + response shapes used by your account. Map JSON fields to the models here.
- Add exponential backoff/retry for HTTP 429/5xx (wrap URLSession in a small Retrier).
- Add persistent local cache (Core Data/SQLite) + background sync; use `modified_since` to limit payload size.
- Add roles/permissions (employee vs. admin). Hide admin-only actions.
- Add error telemetry + structured logging.
- Add unit/UI tests for auth, sync, and clock workflows.
- Ensure least-privilege scopes and in-app sign-out/token revocation.
*/
