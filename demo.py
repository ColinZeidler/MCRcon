import getpass
import mcrcon

print('Ctrl-C to exit')
host = input('Host: ')
port = input('Port (25575): ')
if port == '': 
    port = 25575
else: 
    port = int(port)
pwd = getpass.getpass('Password: ')

print("Connecting...")
r = mcrcon.MCRcon(host, port, pwd)
print("Logged in successfully")

try:
    while True:
        line = input('Rcon: ')
        print(r.send(line))
except KeyboardInterrupt as e:
    r.close()
