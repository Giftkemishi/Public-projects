import subprocess

def get_wifi_password():
    try:

        data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode()
        profiles = [i.split(":")[1][1:-1] for i in data.split("\n") if "All User Profile" in i]
        for i in profiles:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode()
            lines = results.split("\n")
            password = None
            for line in lines:
                if "Key Content" in line:
                    password = line.split(":")[1][1:-1]
            print("Network Name: ", i)
            print("Password: ", password)
    except Exception as e:
        print(e)

get_wifi_password()

