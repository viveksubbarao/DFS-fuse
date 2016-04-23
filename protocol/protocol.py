import socket
import sys
import json
import os
from datetime import datetime
from stat import *
import heartbeat

#server's hostname here
host = socket.gethostname()
# port = 50007 		# communicate protocol.py to server.py
port = 50008 		# communicate protocol.py to master.py

#command_dict 	   = {'create':1 , 'read':2 , 'write' :3 }
#rever_command_dict = {1:'create', 2:'read' ,3: 'write'}


def send_command(command, param_list):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))

	command_string = stringify_command(command, param_list)
	
	s.send(command_string)
	s.close()


def listen_for_command():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(('', port))
	s.listen(10)

	while True:
	  conn, addr = s.accept()
	  print 'client connected ... ', addr
	  #myfile = open('testfile.mov', 'w')

	  while True:
	    data = conn.recv(1000000)
	    if not data: break
	    execute_json_command(data)
	    #print 'writing file ....'

#returns a serialized json string with the command and parameters

def rmdir(self, path):
	print 'self: '+str(self)
	print 'path: ' +str(path)

def mkdir(path, mode):
	# print 'self: ' + str(self)
	print 'path: '+str(path)
	print 'mode: '+str(mode)

# this method updates the data strucutre for the heartbeat times

def heartBeat(servername,idontknow):
	print 'in heartbeat function '+idontknow
	heartbeat.heartBeatTimes[servername] = datetime.now()
	heartbeat.serverStatus[servername] = 'alive'
	#print heartbeat.heartBeatTimes
	#print heartbeat.serverStatus

def stringify_command(command, param_list):
	commandObj = {}
	#commandObj['command'] = command_dict.get(command)
	commandObj['command'] = command
	commandObj['param_list'] = param_list
	
	print json.dumps(commandObj)
	return json.dumps(commandObj)


def execute_json_command(command_string):
	#print 'in execute_json_command'
	commandObj = json.loads(command_string)
	param_list = commandObj['param_list']

	command = commandObj['command']
	print 'executing '+ command +' and passing parameter list ' + param_list
	eval(command)(*param_list)



# execute_json_command(stringify_command('mkdir',['/Users/chen/Repository/PythonProjects/HelloPython/protocol test/TestMkDir', 0755]))
# send_command('mkdir',['/Users/chen/Repository/PythonProjects/HelloPython/protocol test/TestMkDir', 0755])

# path = os.getcwd() + '/common.py'
# send_command('access', [path, os.F_OK])

path = os.getcwd() + '/tempfile.txt'
mode = S_IRUSR
# send_command('chmod', [path, mode])

path = os.getcwd() + '/tempfile.txt'
uid = 1
gid = 1
# send_command('chown', [path, uid, gid])

path = os.getcwd() + '/tempfile.txt'
attr = 'name'
# send_command('getattr', [path, attr])

path = os.getcwd()
# send_command('readdir', [path])

dst = '/tmp/python'
# send_command('readlink', [dst])

# send_command('unlink', [dst])

dst = '/tmp/python'
src = '/usr/bin/python'
# send_command('symlink', [src, dst])

filename = '/tmp/tmpfile'
mode = S_IRUSR
dev = os.makedev(10, 20)
# send_command('mknod', [filename, mode])  # invalid

path = os.getcwd() + '/newDir'
mode = 0755
# send_command('mkdir', [path, mode])

path = os.getcwd() + '/newDir'
# send_command('rmdir', [path])

path = os.getcwd()
# send_command('statfs', [path])

fileOld = os.getcwd() + '/file.txt'
fileNew = os.getcwd() + '/file1.txt'
# send_command('rename', [fileOld, fileNew])
# send_command('rename', [fileNew, fileOld])

# send_command('link', [fileOld, fileNew])  # invalid

# stinfo = os.stat(fileOld)
# times = (1500000000.0, 1500000000)
# send_command('utime', [fileOld, (1500000000.0, 1500000000)])

# send_command('open', [fileOld, os.O_RDWR | os.O_CREAT])

# send_command('create', [fileNew, S_IRUSR | S_IWUSR])

fd = os.open(fileOld, os.O_RDWR)
offset = 5
length = 5  # read from 6-10
# send_command('read', [fileOld, length, offset, fd])
os.close(fd)

fd = os.open(fileOld, os.O_RDWR)
offset = 10
buf = 'LOL'  # read from 6-10
# send_command('write', [fileOld, buf, offset, fd])
os.close(fd)

# send_command('truncate', [fileOld, 10])

fd = os.open(fileOld, os.O_RDWR)
# send_command('flush', [fileOld, fd])
os.close(fd)

### Test access in 50008
path = os.getcwd() + '/common.py'
#send_command('access', [path, os.F_OK])

path = os.getcwd()
# send_command('readdir', [path])

# send_command('', [])

