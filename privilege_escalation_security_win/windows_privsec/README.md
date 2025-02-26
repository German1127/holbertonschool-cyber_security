# 0. Privilege Escalation in Windows Environments  

## Objective  

Your goal is to extract sensitive data from unattended files.  

**Your target machine is Virtual Machine (VM): LAB01**  

- To locate unattended installation files, extract sensitive administrative credentials, and covertly gain access to retrieve a target flag.  
- The password for the student account is: **Student**  
- The following steps detail the functionality of the Python script and its execution process.  

Write a script to resolve this task.  

---

## 1. Typical File Locations  

The script scans the following common locations for unattended installation files:  

- `sysprep.inf`  
- `autounattend.xml`  
- `Unattend.xml`  

---

## 2. Password Extraction  

Utilizes regular expressions to extract the following pattern from the files:  

```
<AdministratorPassword>  
    <Value>(.*?)</Value>  
</AdministratorPassword> 
```

## 3. Decoding

Decodes the extracted password.

## 4. Admin Session

Uses ** runas ** to establish an administrative session using the extracted credentials. to get the flag which is in the desktop of the Admin session

---

# 1. Privilege Escalation via SAM & SYSTEM Backup Files   

## Objective  

Your objective is to exploit a vulnerability in the system to recover the superAdministrator password and retrieve the flag.  

**Your target machine is Virtual Machine (VM): LAB02**  

- The password for the Sammy account is:  

  **Sammy**  

---

## Steps to Complete  

### 1. Privilege Enumeration  
- Download and run the **PrivCheck** PowerShell script on the target system.  
- Analyze the output to identify the vulnerability.  

### 2. Research and Exploitation  
- Research the vulnerability online.  
- Locate and download a working vulnerability file `.exe` exploit.  
- Use the exploit to extract critical files from the target system.  

### 3. Hash Extraction  
- Switch to **Kali Linux** and ensure the **Impacket** toolkit is installed.  
- Use the `secretdump.py` tool to extract hashed passwords from the files.  

### 4. Administrator Session Access  
- Use the recovered hashes to open an **Administrator session**.  
- Obtain the flag from the session and save it.  

---

# 2. Hijack the Service - Exploit Weak Permissions  

## Your target machine is Virtual Machine (VM): LAB03  

- The password for the student account is: **Student**  

A service running with elevated privileges has weak file permissions. You’ve identified that it loads a DLL from a writable directory, giving you an opportunity to hijack it and escalate your privileges.  

Can you hijack the service by exploiting the weak permissions and loading a malicious DLL to gain **SYSTEM** access?  

Try to use this to get the flag from the superAdministrator:  

### Example of DLL code:  

**SprintCSPDLL**  

### Use Windows 10 RpcClient to execute the DLL:  

**WIN10RpcClient.exe**  


## Steps to Complete  

### 1. Run privcheck  
- Execute **privcheck** in the terminal to check for services with weak permissions.  

### 2. Check for writable path  
- Review **privcheck** output for any writable paths.  

### 3. Generate a DLL  
- Create a DLL file.  
- Write code to add a user with **admin privileges**.  
- Compile the DLL.  

### 4. Copy DLL to Confluence bin  
- Copy the DLL to the writable paths.  

### 5. Trigger DLL with RPCClient  
- Use **RPCClient** to load and execute the DLL.  

### 6. Retrieve flag  
- **Flag Location:** `C:\User\superAdministrator\Desktop`  

---

# 3. PowerShell Transcript Files Lab  

## Your target machine is Virtual Machine (VM): LAB04  

- The password for the student account is: **Student**  

---

## Steps to Complete  

### 1. Understand the PowerShell Transcription Environment  
- Ensure transcription is configured and active on your system.  

### 2. Locate PowerShell Transcript Files  
- Search for PowerShell transcript files on the system to identify their location.  

### 3. Analyze Privilege Escalation Opportunities  
- Analyze the transcript files for any evidence of privilege escalation or unauthorized actions that might have been executed through the exploitation of the transcript logs.  

### 4. Locate the Hidden Flag  
- Search the transcript files for any concealed flags, potentially hidden within command outputs or injected data.  
