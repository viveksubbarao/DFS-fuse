import threading
import time
from datetime import datetime
from protocol import *
from common import *

########## data structues to track heartbeats and server status ##############

global heartBeatTimes
heartBeatTimes = {}
global serverStatus 
serverStatus = {}

curr_server_sock = [server1_sock]
curr_server = 0;

def get_curr_server():
    global curr_server_sock, curr_server
    return curr_server_sock[curr_server]

# this method updates the data strucutre for the heartbeat times
def heartBeat(servername):
    #print 'in heartbeat function '#+idontknow
    heartBeatTimes[servername[0]] = datetime.now()
    serverStatus[servername[0]] = 'alive'
    #print heartbeat.heartBeatTimes
    #print heartbeat.serverStatus

## this cass would have to be imported into the server processes and the heartbeat emitter threat would emit  
##  heartbeats
def heartBeatEmitter(threadName):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, M_PORT))
    while True:
        time.sleep(1)
        #print 'Emitting heart beats from '+ threadName
        send_command(s, 'heartbeat', [threadName])


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
    #print 'checking initiated at master'

    while True:
        time.sleep(1)
        #print 'checking initiated at master'
        print 'serverstatus ' + str(serverStatus)
        #print 'heartbeattimes' + str(heartBeatTimes)
        for server in heartBeatTimes:
            delta = datetime.now() - heartBeatTimes[server] 
            if delta.total_seconds() > timeout:
                serverStatus[server] = 'dead'
                #insert call to method that will try reviving it 





class heartBeatCheck(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

        #self.name = name
        
    def run(self):        
        heartBeatChecker()
