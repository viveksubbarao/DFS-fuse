import threading
import time
from datetime import datetime
from protocol import *


########## data structues to track heartbeats and server status ##############

global heartBeatTimes
heartBeatTimes = {}
global serverStatus 
serverStatus = {}

## this cass would have to be imported into the server processes and the heartbeat emitter threat would emit  
##  heartbeats
def heartBeatEmitter(threadName):
    
    while True:
        time.sleep(1)
        print 'Emitting heart beats from '+ threadName
        send_command('heartbeat',[threadName])


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
    print 'checking initiated at master'
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


#this method checks datastructures that track the last heartbeattimes and update the serverstatus ds incase the heartbeats 
#have time out indicating that the process is no longer available and try to revive them 








#t1 =  myThread('thread1',5)
#t2=  myThread('thread2',5)

#t1.start()
#t2.start()
