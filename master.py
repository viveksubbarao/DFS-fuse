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

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50008              # Arbitrary non-privileged port
N1 = 50009
N2 = 50010

conn_db = ''

def execute_json_command(conn, command_string):
    commandObj = json.loads(command_string)
    param_list = commandObj['param_list']
    command = commandObj['command']
    if command == 'heartbeat':
        heartBeat(param_list)
    else:
        send_command(command, param_list)

def send_command(command, param_list):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), N1))

    command_string = stringify_command(command, param_list)
    
    s.send(command_string)
    journaling(command, param_list, 'N1')
    s.close()

def receiving(conn_db):
    print 'Receiving commands'
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)

    while 1:
        conn, addr = s.accept()
        print 'Connected by: ', addr

        while 1:
            data = conn.recv(1024)
            if not data:
                break
            execute_json_command(conn, data)

    # release source
    conn.close()
    s.close()


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
    print "Connecting to database\n ->%s" % (conn_string)
 
    # get a connection, if a connect cannot be made an exception will be raised here
    conn_db = psycopg2.connect(conn_string)
 
    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    # cursor = conn.cursor()
    print "Connected!\n"
    return conn_db
 
if __name__ == "__main__":
    conn_db = connection()
    receiving(conn_db)

