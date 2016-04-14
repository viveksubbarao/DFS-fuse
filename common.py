import socket
import sys
import json
import os
import logging

logging.basicConfig(stream=sys.stderr, format='%(asctime)s - %(levelname)s - %(message)s')
log = logging.getLogger()
log.setLevel(logging.DEBUG)

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

def _decode_list(data):
    rv = []
    for item in data:
        if isinstance(item, unicode):
            item = item.encode('utf-8')
        elif isinstance(item, list):
            item = _decode_list(item)
        elif isinstance(item, dict):
            item = _decode_dict(item)
        rv.append(item)
    return rv

def _decode_dict(data):
    rv = {}
    for key, value in data.iteritems():
        if isinstance(key, unicode):
            key = key.encode('utf-8')
        if isinstance(value, unicode):
            value = value.encode('utf-8')
        elif isinstance(value, list):
            value = _decode_list(value)
        elif isinstance(value, dict):
            value = _decode_dict(value)
        rv[key] = value
    return rv
    
def send_and_recv(conn, command, param_list):
    command_string = stringify_command(command, param_list)
    conn.send(command_string)
    
    result = conn.recv(1000)
    res = json.loads(result, object_hook=_decode_dict)
    return res

#returns a serialized json string with the command and parameters
def stringify_command(command, param_list):
	commandObj = {}
	commandObj['command'] = command
	commandObj['param_list'] = param_list
	
	return json.dumps(commandObj)

#returns a serialized json string with the command and parameters
def stringify_result(ret):
	return json.dumps(ret)