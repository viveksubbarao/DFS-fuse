import socket
import sys
from time import sleep

HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server

f= open(sys.argv[1],"rb")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
#count = 1;
#while 1:
	#s.sendall(str(count))
s.sendall(f.read())

sleep(1);

f.close()
#data = s.recv(1024)
s.close()
#print 'Received', repr(data)
print 'sent file to srever'