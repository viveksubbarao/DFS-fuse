#!/usr/bin/python
import socket
import psycopg2
from heartbeat import *
from common import *





checkheartbeat = heartBeatCheck()
checkheartbeat.daemon = True
checkheartbeat.start()

with open('credentials.txt', 'r') as f:
    credentials = f.readline().split(':')
    print credentials

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50008              # Arbitrary non-privileged port

i = 0
'''def execute_json_command(conn, command_string):
    commandObj = json.loads(command_string)
    param_list = commandObj['param_list']
    command = commandObj['command']
    print i
    print command'''
i += 1


print 'connecting...'
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
        #execute_json_command(conn, data)
        execute_json_command( data)

# release source
conn.close()
s.close()

def main():
    #Define our connection string
    dbname = credentials[0]
    username = credentials[1]
    password = credentials[2]
    host = credentials[3]
    conn_string = "host='" + host + "' dbname='" + dbname + "' user='"+ username +"' password='" + password + "'"
 
    # print the connection string we will use to connect
    print "Connecting to database\n ->%s" % (conn_string)
 
    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)
 
    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
    print "Connected!\n"
 
if __name__ == "__main__":
    main()
