import threading
import time
from datetime import datetime
from protocol import *

## this cass would have to be imported into the server processes and the heartbeat emitter threat would emit  
##  heartbeats

class hearBeatEmit (threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        
        self.name = name
        
    def run(self):        
        hearBeatEmitter(self.name)
       

def hearBeatEmitter(threadName):
    while True:
        time.sleep(10)
        send_command('hearBeat',[threadName])

        
## this class would have to be imported into the server manager and the hearBeatChecker method could be called
# to check if any heartbeat has timeout

class hearBeatChecker(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)

        self.name = name
        
    def run(self):        
        heartBeatChecker(self.name)        


#this method checks datastructures that track the last heartbeattimes and update the serverstatus ds incase the heartbeats 
#have time out indicating that the process is no longer available and try to revive them 

def heartBeatChecker(threadName):
    timeout = 100
    while True:
        time.sleep(10)
        
        for server in heartBeatTimes:
            delta = datetime.now() - heartTimes[server] 
            if delta.total_seconds() > timeout:
                serverStatus[server] = 'dead'
                #insert call to method that will try reviving it 










#t1 =  myThread('thread1',5)
#t2=  myThread('thread2',5)

#t1.start()
#t2.start()
