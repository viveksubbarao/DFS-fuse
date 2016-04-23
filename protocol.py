import socket
import sys
import json 
from datetime import datetime


#server's hostname here
host = socket.gethostname()
port = 8080


#command_dict 	   = {'create':1 , 'read':2 , 'write' :3 }
#rever_command_dict = {1:'create', 2:'read' ,3: 'write'}


def send_command(command,param_list):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))

	command_string = stringify_command(command,param_list)
	
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

	    #print 'writing file ....'


#returns a serialized json string with the command and parameters

def rmdir(self, path):
	print 'self'+str(self)
	print 'path' +str(path)

def mkdir(self, path, mode):
	print 'self' + str(self)
	print 'path'+str(path)
	print 'mode'+str(mode)

# this method updates the data strucutre for the heartbeat times

def heartBeat(servername):
	heartBeatTimes[servername] = datetime.now()
	serverStatus[servername] = 'alive'


def stringify_command(command, param_list):
	commandObj = {}
	#commandObj['command'] = command_dict.get(command)
	commandObj['command'] = command
	commandObj['param_list'] = param_list
	
	print json.dumps(commandObj)
	return json.dumps(commandObj)


def execute_json_command(command_string):
	commandObj = json.loads(command_string)
	param_list = commandObj['param_list']

	command = commandObj['command']
	eval(command)(*param_list)



#execute_json_command( stringify_command('mkdir',['selfie',2,'moodu']))

########## data structues to track heartbeats and server status ##############

heartBeatTimes = {}
serverStatus = {}