import socket
import sys
import json
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

''''
DFS_CHMOD:,
DFS_CHOWN:,
DFS_GETATTR:,
DFS_READDIR:,
DFS_READLINK:,
DFS_MKNOD:,
DFS_RMDIR:,
DFS_MKDIR:,
DFS_STATFS:,
DFS_UNLINK:,
DFS_SYMLINK:,
DFS_RENAME:,
DFS_LINK:,
DFS_UTIMES:,
DFS_OPEN:,
DFS_CREATE:,
DFS_READ:,
DFS_WRITE:,
DFS_TRUNCATE:,
DFS_FLUSH:,
DFS_RELEASE:,
DFS_FSYNC:
}
'''
def send_and_recv(conn, command, param_list):
    print(command, param_list)
    command_string = stringify_command(command, param_list)
    print(command_string)
    conn.send(command_string)
    
    result = conn.recv(1000)
    print(result)
    
    #resObj = {}
    res = json.loads(result)
    print res
    return res
	#res_data = resObj['data']
	#retval = resObj['retval']
    ''''
    if retval:
        return retval
    else:
        return res_data
    '''

#returns a serialized json string with the command and parameters
def stringify_command(command, param_list):
	commandObj = {}
	commandObj['command'] = command
	commandObj['param_list'] = param_list
	
	print json.dumps(commandObj)
	return json.dumps(commandObj)

#returns a serialized json string with the command and parameters
def stringify_result(ret):
	#resObj = {}
	#resObj['retval'] = retval
	#resObj['data'] = data
	
	print json.dumps(ret)
	return json.dumps(ret)