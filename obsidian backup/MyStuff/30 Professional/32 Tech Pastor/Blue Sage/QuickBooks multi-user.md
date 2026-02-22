Here’s the clean, practical way to set up **QuickBooks in multi-user mode for a small office**, without overcomplicating it.

---

## **✅ What “Multi-User” Means in QuickBooks**

  

Multi-user mode lets **multiple people work in the same company file at the same time**—for example, one person invoicing while another runs payroll.

  

This applies to:

- [QuickBooks Desktop](chatgpt://generic-entity?number=0) (Windows or Mac)
    
- Not needed for [QuickBooks Online](chatgpt://generic-entity?number=1) (it’s already multi-user by design)
    

  

Everything below assumes **QuickBooks Desktop**.

---

## **🖥️ What You Need (Minimum Requirements)**

  

### **1. One Main “Host” Computer (or Server)**

- Stores the **actual company file (.QBW)**
    
- Runs:
    
    - [QuickBooks Desktop](chatgpt://generic-entity?number=2)
        
    - **QuickBooks Database Server Manager**
        
    

  

### **2. Local Office Network**

- All computers on the **same LAN**
    
- Wired Ethernet is strongly preferred over Wi-Fi
    

  

### **3. Same QuickBooks Version on Every Computer**

- Example: Everyone must be on **QuickBooks Desktop Pro 2024**
    
- Same **year**, same **edition**
    

---

## **🛠️ Step 1 — Install Database Server Manager on the Host**

  

On the host computer:

1. Run the QuickBooks installer
    
2. Choose:
    
    > **“Install Database Server Only”**
    
3. After install, open:
    
    - **QuickBooks Database Server Manager**
        
    
4. Add the folder that holds your .QBW file
    
5. Click **Scan**
    

  

✅ This opens the file to the network.

---

## **👤 Step 2 — Create Users (On the Host)**

  

In QuickBooks:

```
Company → Users → Set Up Users and Roles
```

Add each person with:

- Username
    
- Password
    
- Proper role (Admin, AR/AP, Payroll, etc.)
    

---

## **📂 Step 3 — Put the Company File in a Shared Folder**

  

Example:

```
\\OfficeServer\QuickBooks\Company.qbw
```

Make sure:

- Everyone has **read/write permissions** to that folder
    
- Not just read-only
    

---

## **🔄 Step 4 — Turn On Multi-User Mode**

  

On the **host computer**:

```
File → Switch to Multi-User Mode
```

Every other workstation:

```
File → Open or Restore Company → Open a Company File → Network
```

Then browse to the shared folder and open the file.

---

## **🔐 Step 5 — Firewall Rules (Very Common Failure Point)**

  

Open these ports on the host firewall:

|**Year**|**Port**|
|---|---|
|2022|8019|
|2023|8020|
|2024|8021|

Also allow:

- QBDBMgrN.exe
    
- QBCFMonitorService.exe
    

  

If you skip this step, users will get:

  

> “H202 / H505 Network Error”

---

## **⚠️ Important Limitations**

- ❌ Two users **cannot edit the same transaction at the same time**
    
- ✅ Different areas (billing, payroll, reports) usually work fine
    
- ❌ QuickBooks **Mac multi-user is weaker** than Windows
    
- ✅ Best reliability is **all Windows**
    

  

If you’re mixing platforms:

- [Windows](chatgpt://generic-entity?number=3) works best as the host
    
- [macOS](chatgpt://generic-entity?number=4) may have connection drops
    

---

## **✅ Alternative (Often Better for Small Offices)**

  

If you **don’t need Desktop-only features**, switching to:

- [QuickBooks Online](chatgpt://generic-entity?number=5)
    

  

Benefits:

- No server
    
- No port forwarding
    
- Works from any location
    
- Easier backups
    
- Built-in multi-user
    

---

## **✅ My Recommendation for a Small Office**

  

If this is:

- **2–5 users**
    
- Same physical office
    
- Existing Desktop licenses
    

  

👉 Use **QuickBooks Desktop + Database Server Manager**

  

If this is:

- **Remote staff**
    
- Field workers
    
- Mac + Windows mix
    

  

👉 Use **QuickBooks Online**

---

If you want, you can tell me:

- ✅ How many users?
    
- ✅ Windows, Mac, or mixed?
    
- ✅ Desktop Pro, Premier, or Enterprise?
    

  

And I’ll map the **exact best setup for your office** without guesswork.