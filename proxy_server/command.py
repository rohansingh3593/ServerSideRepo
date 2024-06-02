# content for WIFI Password check.

import subprocess
import os

def get_profiles():
    try:
        meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])
        data = meta_data.decode('utf-8', errors="backslashreplace")
        data = data.split('\n')
        return data
    except subprocess.CalledProcessError as e:
        log_error(f"Error occurred while fetching profiles: {e}")
        return []

def parse_profiles(data):
    profiles = []
    for i in data:
        if "All User Profile" in i:
            i = i.split(":")
            i = i[1]
            i = i[1:-1]
            profiles.append(i)
    return profiles

def get_password(profile):
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear'])
        results = results.decode('utf-8', errors="backslashreplace")
        results = results.split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        if results:
            return results[0]
        else:
            return ""
    except subprocess.CalledProcessError as e:
        log_error(f"Error occurred while fetching password for {profile}: {e}")
        return "Encoding Error Occurred"
    except IndexError:
        return ""

def log_error(message):
    with open("wifi_passwords.log", "a") as log_file:
        log_file.write(f"{message}\n")

def log_output(message):
    with open("wifi_passwords.log", "a") as log_file:
        log_file.write(f"{message}\n")

def main():
    data = get_profiles()
    profiles = parse_profiles(data)

    log_output("{:<30}| {:<}".format("Wi-Fi Name", "Password"))
    log_output("----------------------------------------------")

    for profile in profiles:
        password = get_password(profile)
        log_output("{:<30}| {:<}".format(profile, password))

if __name__ == "__main__":
    main()



"""
pyinstaller command.py --onefile

"""
