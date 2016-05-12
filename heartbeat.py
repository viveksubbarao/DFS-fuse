import threading
import time

from datetime import datetime
from common import *

########## data structues to track heartbeats and server status ##############

global heartBeatTimes
heartBeatTimes = {}
global serverStatus 
serverStatus = {}
global aliveServerSet 
aliveServerSet = set()
aliveServerNumber = 0

###### this function helps to identify which runing 'alive' server should be picked for performing the operations######
def getRandomAliveServer():
    global aliveServerNumber
    listOfAliveServers = list(aliveServerSet)
    if len(listOfAliveServers) != 0:
        #print listOfAliveServers[0]
        server_tuple = listOfAliveServers[0]
        serverName = listOfAliveServers[0][0]
        server_conn_obj = listOfAliveServers[0][1]
        #print server_conn_obj.getpeername()
        return str(server_conn_obj.getpeername()[0])+','+str(server_port[serverName])
    return 'None'


# this method updates the data strucutre for the heartbeat times
def heartBeat(conn,servername):
    #print conn.getpeername()    
    heartBeatTimes[servername[0]] = datetime.now()
    serverStatus[servername[0]] = ('alive',conn)
    aliveServerSet.add((servername[0],conn))
    log.debug(heartBeatTimes)
    log.debug(serverStatus)

## this cass would have to be imported into the server processes and the heartbeat emitter thread would emit  
##  heartbeats
def heartBeatEmitter(threadName):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, M_PORT))
    while True:
        time.sleep(3)
        log.debug('Emitting heart beats from '+ threadName)
        command_string = stringify_command('heartbeat', [threadName])
        s.send(command_string)
    s.close()



class heartBeatEmit(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        
        self.name = name
        
    def run(self):        
        heartBeatEmitter(self.name)
        
## this class would have to be imported into the server manager and the hearBeatChecker method could be called
# to check if any heartbeat has timeout

def heartBeatChecker():
    timeout = 3
    log.debug('checking initiated at master')

    while 1:
        time.sleep(3)
        #comment this out
        #print 'randomly retuned' + str(getRandomAliveServer())
        log.debug('serverstatus ' + str(serverStatus))
        print 'serverstatus ' + str(serverStatus)
        print 'alive set '+ str(aliveServerSet)
        log.debug('heartbeattimes' + str(heartBeatTimes))
        for server in heartBeatTimes:
            delta = datetime.now() - heartBeatTimes[server] 
            if delta.total_seconds() > timeout:
                conn_obj = serverStatus[server][1]
                #print serverStatus[server]
                serverStatus[server] = ('dead',conn_obj)
                #print server+' has died'
                aliveServerSet.discard((server,conn_obj))


class heartBeatCheck(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        aliveServerNumber = 0
        
    def run(self):        
        heartBeatChecker()
