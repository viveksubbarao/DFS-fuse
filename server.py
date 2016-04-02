# Echo server program
import socket
import os

# Filesystem methods
DFS_ACCESS = 1
DFS_CHMOD = 2
DFS_CHOWN = 3
DFS_GETATTR = 4
DFS_READDIR = 5
DFS_READLINK = 6
DFS_MKNOD = 7
DFS_RMDIR = 8
DFS_MKDIR = 9
DFS_STATFS = 10
DFS_UNLINK = 11
DFS_SYMLINK = 12
DFS_RENAME = 13
DFS_LINK = 14
DFS_UTIMES = 15

# File methods
DFS_OPEN = 16
DFS_CREATE = 17
DFS_READ = 18
DFS_WRITE = 19
DFS_TRUNCATE = 20
DFS_FLUSH = 21
DFS_RELEASE = 22
DFS_FSYNC = 23

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

while 1:
    conn, addr = s.accept()
    print 'Connected by ', addr
    data = conn.recv(64)
    print data, len(data)
    conn.close()

s.close()

''''
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

#f.close()
conn.close()
'''