#!/usr/bin/python
import socket
import psycopg2

from heartbeat import *
from common import *
from datetime import datetime

checkheartbeat = heartBeatCheck()
checkheartbeat.daemon = True
checkheartbeat.start()

with open('credentials.txt', 'r') as f:
    credentials = f.readline().split(':')
    print credentials

def process_command(conn):
    while 1:
        data = conn.recv(1024)
        if not data:
            break
        execute_command(conn, data)
    conn.close()

def execute_command(conn, command_string):
    log.debug("executing command")
    commandObj = json.loads(command_string)
    param_list = commandObj['param_list']
    command = commandObj['command']
    if command == 'heartbeat':
        heartBeat(param_list)
    else:
        send_command(conn, command, param_list)

def receiving(conn_db):
    log.debug('Receiving commands')
    global client_sock
    
    # Create listening socket
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.bind((HOST, M_PORT))
    client_sock.listen(1)

    # Spawn a thread for each new request. This means that a new thread is
    # spawned for each client as well as each server.
    while 1:
        conn, addr = client_sock.accept()
        log.debug('Connected by: %s', addr)
        threading.Thread(target=process_command, args=(conn,)).start()

    # release source
    client_sock.close()


def journaling(command, param_list, server_id):
    if conn_db is None:
        print 'Connection error'
        exit(1)

    cursor = conn_db.cursor()
    print param_list[0][param_list[0].rindex('/') + 1 : ]
    sql = 'INSERT ' \
        + 'INTO dfs_journal(filename, N1, N2) ' \
        + 'VALUES(\'' + param_list[0][param_list[0].rindex('/') + 1 : ] + '\', CURRENT_TIMESTAMP, null);'
    cursor.execute(sql)
    conn_db.commit()

def connection():
    global conn_db

    #Define our connection string
    dbname = credentials[0]
    username = credentials[1]
    password = credentials[2]
    host = credentials[3]
    conn_string = "host='" + host + "' dbname='" + dbname + "' user='"+ username +"' password='" + password + "'"
 
    # print the connection string we will use to connect
    log.debug("Connecting to database " + conn_string)
 
    # get a connection, if a connect cannot be made an exception will be raised here
    conn_db = psycopg2.connect(conn_string)
 
    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    # cursor = conn.cursor()
    log.debug("Connected!")
    return conn_db
 
if __name__ == "__main__":
    conn_db = connection()
    receiving(conn_db)

