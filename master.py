#!/usr/bin/python
import socket
import pickle
from common import *
from heartbeat import *
from protocol import *
from datetime import datetime
from dispatch import *

checkheartbeat = heartBeatCheck()
checkheartbeat.daemon = True
checkheartbeat.start()

checkdispatch = dispatchCheck()
checkdispatch.daemon = True
checkdispatch.start()

def process_command(conn):
    while 1:
        data = conn.recv(1024)
        if not data:
            break
        execute_command(conn, data)
    conn.close()

def send_server_obj(conn):
    #print 'in send_server_obj'
    #print getRandomAliveServer()
    #conn.send(pickle.dumps(getRandomAliveServer(),-1))
    #print conn.getpeername()
    conn.send(getRandomAliveServer())

    

def execute_command(conn, command_string):
    commandObj = json.loads(command_string)
    param_list = commandObj['param_list']
    command = commandObj['command']
    if command == 'heartbeat':
        heartBeat(conn,param_list)
    elif command == 'connect':
        send_server_obj(conn)
    #else:
    #    send_command(conn, command, param_list)

def receiving():
    log.debug('Receiving commands')
    global client_sock
    
    # Create listening socket
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    client_sock.bind((HOST, M_PORT))
    client_sock.listen(1)

    # Spawn a thread for each new request. This means that a new thread is
    # spawned for each client as well as each server.
    while 1:
        conn, addr = client_sock.accept()
        log.debug('Connected by: %s', addr)
        th = threading.Thread(target=process_command, args=(conn,))
        th.daemon =  True
        th.start()
    # release source
    client_sock.close()

if __name__ == "__main__":
    receiving()
