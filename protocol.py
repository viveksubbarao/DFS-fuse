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

    # Get currently used servers communication socket
    # TODO - make this generic. The heartbeat infrastructure should
    # give us the current active servers socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((HOST, S1_PORT))

    # Send the JSON command + param string
	sock.send(command_string)

	data = sock.recv(1024)

	# Get back the reply from the server
	conn.send(data)

	# Send the reply back to the client. This is like a passthrough procedure
    # where the master does not handle the reply.
	sock.close()

    # Log the command to the journal
    # TODO: here default storage server is N1, should choose based on heartbeat
    # journaling(conn_db, command, param_list, 'N1')

def journaling(conn_db, command, param_list, server_id):
    if conn_db is None:
        print 'Connection error'
        exit(1)

    cursor = conn_db.cursor()
    print param_list[0][param_list[0].rindex('/') + 1 : ]
    if server_id == 'N1':
        sql = 'INSERT ' \
            + 'INTO dfs_journal(filename, N1, N2) ' \
            + 'VALUES(\'' + param_list[0][param_list[0].rindex('/') + 1 : ] + '\', CURRENT_TIMESTAMP, null);'
    elif server_id == 'N2':
        sql = 'INSERT ' \
            + 'INTO dfs_journal(filename, N1, N2) ' \
            + 'VALUES(\'' + param_list[0][param_list[0].rindex('/') + 1 : ] + '\', null, CURRENT_TIMESTAMP);'
    cursor.execute(sql)
    # log.debug('SQL  ' + sql)
    conn_db.commit()

def send_and_recv(conn, command, param_list):
	# log.debug('send_and_recv')
	command_string = stringify_command(command, param_list)
	conn.send(command_string)
	log.debug('command sent')

	result = conn.recv(1000)
	log.debug('res recv')
	res = json.loads(result)
	return res