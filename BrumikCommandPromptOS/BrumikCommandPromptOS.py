import random
import time
import sys
import os
import calendar
import platform
import subprocess
import winreg

# Proměnné
username = ""
password = ""
user = ""
system_name = platform.system()
platform_open = ""
platform_app_path = ""
settings_system_name = ""

# Definitions
def OS():
    if system_name == "Darwin":
        settings_system_name = "macOS"
    elif system_name == "Windows":
        settings_system_name = "Windows"
    elif system_name == "Linux":
        settings_system_name = "Linux"

def clear():
    if system_name == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def open_app(open_app):
    print(open_app)

def login():
    clear()
    print("Welcome to Brumik Command Prompt OS!")
    time.sleep(2)
    clear()
    print("Enter your username (if you don't have account type 'guest'):")
    username = input()
    if username == "guest":
        menu()
    clear()
    print("Enter your password:")
    password = input()
    if username == "Brumik" and password == "BrumikCMD1234":
        user = username
        menu()
    else:
        clear()
        print("Invalid username or password!")
        time.sleep(3)
        login()

def menu():
    clear()
    print("Brumik Command Prompt OS:")
    print("[1] Command Prompt")
    print("[2] Account Informations")
    print("[3] Logout")
    print("[4] Applications")
    print("[5] Settings")
    print("[6] File Manager")
    print("[7] Exit")

    program = input()
    if program == "1":
        open_app("CMD")
    elif program == "2":
        acc_info()
    elif program == "3":
        user = ""
        username = ""
        password = ""
        login()
    elif program == "4":
        applications()
    elif program == "5":
        settings()
    elif program == "6":
        file_manager()
    elif program == "7":
        sys.exit()

def applications():
    comingsoon("Application folder")

def settings():
    clear()
    print("OS info: 1.0")
    print(f"PC Operating System: {settings_system_name}")
    exit = input("(y/n) >>>")
    if exit == "y":
        menu()
    elif exit == "n":
        settings()

def acc_info():
    clear()
    print(f"Username: {user}")
    print(f"Password: {password}")
    print(" _____ ")
    print("| . . |")
    print("| ___ |")
    print("|_____|")
    print("  | |  ")
    print(" ")
    print("do you want to exit?")
    exit = input("(y/n) >>>")
    if exit == "y":
        menu()
    elif exit == "n":
        acc_info()

def comingsoon(label_comingsoon):
    clear()
    print(f"{label_comingsoon} coming soon!")
    time.sleep(5)
    menu()

# File manager
def file_manager():
    clear()
    print("[1] PC Drive")
    print("[2] System Folders")
    file = input()
    if file == "1":
        if system_name == "Windows":
            subprocess.run(["explorer"], shell=True)
        elif system_name == "Darwin":
            subprocess.run(["open", "/"])
        elif system_name == "Linux":
            subprocess.run(["xdg-open", "/"])
        else:
            print("Nepodporovaný operační systém.")
    elif file == "2":
        def system_folder():
            clear()
            print("[1] Applications")
            print("[2] .bvs")
            file = input()
            if file == "1":
                def application():
                    clear()
                    print("[1] Login")
                    print("[2] Applications")
                    print("[3] Settings")
                    print("[4] Account Info")
                    print("[5] File Manager")
            if file == "2":
                def bvs():
                    clear()
                    print("Folder is Empty!")

# Main Code
clear()
login()