Done! I dropped a ready-to-run SwiftUI scaffold into the canvas:

- OAuth 2.0 + PKCE sign-in (ASWebAuthenticationSession) with Keychain token storage
    
- Minimal API client for /current_user, /jobcodes, /timesheets, plus Clock In/Out stubs
    
- Basic UI: login screen, dashboard with jobcode picker, clock in/out, and today’s entries
    
- Info.plist notes + a quick README with next steps
    

  

Plug in your **Client ID** and **redirect URI** in OAuthConfig, add the URL scheme to your Info.plist, then build and go. If you want me to tailor it to your exact endpoints/fields or swap in Core Data for persistence, say the word and I’ll extend it.