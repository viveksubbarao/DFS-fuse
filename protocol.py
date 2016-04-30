import socket
import sys
import json
import os
from datetime import datetime
from stat import *
from common import *
from heartbeat import *

def send_command(conn, command, param_list):
	# Convert command and parameter list to JSON string
	command_string = stringify_command(command, param_list)

	if (command == 'heartbeat'):
		conn.send(command_string)
 		return

    # Get currently used server
	s_port = getRandomAliveServer()

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((HOST, server_port[s_port]))

    # Send the JSON command + param string
	sock.send(command_string)

	data = sock.recv(1024)

	# Get back the reply from the server
	conn.send(data)

	# Send the reply back to the client. This is like a passthrough procedure
    # where the master does not handle the reply.
	sock.close()


#define new function here 

def send_and_recv(conn, command, param_list):
	#new_connection#get connection object from master 
	log.debug('send_and_recv')
	command_string = stringify_command(command, param_list)
	conn.send(command_string)
	log.debug('command sent')

	result = conn.recv(1000)
	log.debug('res recv')
	res = json.loads(result)
	return res