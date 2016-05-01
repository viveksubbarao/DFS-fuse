import socket
import sys
import json
import os
import pickle
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

#client uses this to get the connection object for the data server
def get_server_conn_obj(conn):
	connect_command = 'connect'
	param_list      = ['null']
	command_string = stringify_command(connect_command, param_list)
	conn.send(command_string)
	server_conn_obj = conn.recv(1000)
	#conn.close()
	return server_conn_obj

def send_and_recv(conn, command, param_list):
	#print 'trying to get server conn obj'
	
	server_conn_obj = str(get_server_conn_obj(conn))
	#print conn_tuple
	
	#server_conn_obj = pickle.loads(get_server_conn_obj(conn))
	#print 'tuple recevied '+ server_conn_obj
	#print 'got server conn obj'
	if server_conn_obj != None:
		log.debug('send_and_recv')
		command_string = stringify_command(command, param_list)
		temp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		temp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		#print 
		ip_socket_list = server_conn_obj.split(',')
		#print 'printing list'+ str(ip_socket_list)
		ip = str(ip_socket_list[0])
		socknumber = int(ip_socket_list[1])

		temp_sock.connect((ip, socknumber))
		temp_sock.send(command_string)
		#print 'command sent'
		result = temp_sock.recv(1000)
		#temp_sock.close()
		#print 'res recv'
		res = json.loads(result)
		return res
	else:
		print 'oops there are no servers to connect to'
		return None

	