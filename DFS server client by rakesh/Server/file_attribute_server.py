# Echo server program
import socket
import os

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.bind((HOST, PORT))
#s.listen(1)
#conn, addr = s.accept()
#print 'Connected by', 

#f = open("cats.png","wb")


while 1:
	print 
	print 'Enter 1 for list of file names'
	print 'Enter 2 for getting proerpties of a file'
	print "Enter 3 for printing contents of a file"
	print 'Enter 4 to exit'
	print 
	choice = int(raw_input('enter choice '))
	if (choice == 1):
		print 
		print os.listdir(os.getcwd())
	elif (choice == 2):
		file_name = str(raw_input('Enter file name '))
		print 
		print os.stat(file_name)
	elif choice ==3:
		file_name = str(raw_input('Enter file name '))
		print 
		print open(file_name).read()
	elif choice ==4 :
		break
	#data = conn.recv(100000)
	

#if not data: break
#conn.sendall(data)

#print 'file received'

f.close()
conn.close()