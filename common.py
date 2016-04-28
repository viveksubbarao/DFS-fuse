import socket
import sys
import json
import os
import logging

logging.basicConfig(stream=sys.stderr, format='%(asctime)s - %(levelname)s - %(message)s')
log = logging.getLogger()
log.setLevel(logging.INFO)

client_sock = -1
server1_sock = -1
server2_sock = -1

HOST = '' # Symbolic name meaning all available interfaces
M_PORT = 50008 # master listening port
S1_PORT = 50009 # server 1 listening port
S2_PORT = 50010 # server 2 listening port
#HB_PORT = 50011 # heartbeat listening port

server_port = {"s1": S1_PORT, "s2": S2_PORT}

DIR_S1 = "s1"
DIR_S2 = "s2"

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
DFS_UTIMENS = 15

# File methods
DFS_OPEN = 16
DFS_CREATE = 17
DFS_READ = 18
DFS_WRITE = 19
DFS_TRUNCATE = 20
DFS_FLUSH = 21
DFS_RELEASE = 22
DFS_FSYNC = 23

#returns a serialized json string with the command and parameters
def stringify_command(command, param_list):
	commandObj = {}
	commandObj['command'] = command
	commandObj['param_list'] = param_list
	
	return json.dumps(commandObj)

#returns a serialized json string with the command and parameters
def stringify_result(ret):
	return json.dumps(ret)
