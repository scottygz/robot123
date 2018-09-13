import threading
import time
import queue
from operator import attrgetter
import random
import abc
import cv2
import numpy as np
import platform
#from matplotlib import pyplot as plt

def bitOn(bits: int , index: int) -> bool : 
    return not ((bits & (1 << index) ) == 0)

class Control:
    actionSequence = []
    timeToGo = 0
    handledBy = ''
    
    def __init__(self, sequence, timeToGo):
        self.actionSequence = sequence
        self.timeToGo = timeToGo
    
    def __str__(self):
        return "Control: time2Go: %s seq: %s Handle:%s" % ( self.timeToGo, self.actionSequence, self.handledBy)
    
class PortIO:
    @abc.abstractmethod
    def turnPort(self, portId: int, onOff: bool):
        return 
    
class PortWrite:
    ports=[]
    def __init__(self, ports):
        self.port = ports
        
    def write(self, port: PortIO, bits: int, maxBits: int= 5):
        for pN in range(min(maxBits, len(self.ports))):
            port.turnPort(self.ports[pN], bitOn(bits, pN))
        pass    
    
    
class ControlThread(threading.Thread):
    lastEventTime = 0  
    timeToStop = 0 
    
    def __init__(self, name, queueIn, queueOut):
        super(ControlThread, self).__init__()
        self.queueIn = queueIn
        self.queueOut = queueOut
        self.name = name
        self.stoprequest = threading.Event()
    
    def sequenceDone(self):
        return True
        pass
        
    def run(self):
        while not self.stoprequest.isSet() :
            try: 
                data = self.queueIn.get(True, 0.05)
                self.lastEventTime = time.clock()
                self.handle(data)
            except queue.Empty:
                self.handleIdle()
                continue
    
    def join(self, timeout=None):
        self.stoprequest.set()
        super(ControlThread, self).join(timeout)

    def handleIdle(self):
        pass
    
    def handle(self, data):
        #print self.name,  data, self.lastEventTime
        data.handledBy = self.name
        time.sleep(random.random()*0.01)
        self.queueOut.put(data)
        pass
    
def openCamera():
    pass

def main(args):
    print("OS Version:", platform.release() )
    print("Starting... ", time.clock())
    qC1 = queue.Queue()
    qF1 = queue.Queue()
    pool = [ControlThread("T-%s" % i, qC1, qF1) for i in range(10)]
    for thread in pool:
        thread.start()
    for i in range(int(args[0])):
        qC1.put(Control([i,2,1,2,3], 10))
    
    for thread in pool:
        thread.join(999)
    print("Finished ", time.clock())
    dall = []
    while True:
        try:
            d = qF1.get(False, 1)
            dall.append(d)
        #    print d
        except queue.Empty:
            print ("Empty now, quit", time.clock())
            break
    sall = sorted(dall, key=attrgetter('actionSequence'))    
    for s in sall:
        #print s
        pass
    
if __name__ == '__main__':
    import sys
    main(sys.argv[1:]) 
    bits = 0xA355
    for i in range(16):
        print( i, bits, bitOn(bits, i))
    cv2_version = cv2.__version__
    print ("OpenCV version:", cv2.__version__)
    cap = cv2.VideoCapture(0)
    
    while(True):
        ret , frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        laplacian = cv2.Laplacian(gray, cv2.CV_64F)
        edges = cv2.Canny(frame, 50,50)
        cv2.imshow('source', gray)
        cv2.imshow('frame', laplacian)
        cv2.imshow('Edges', edges)
        
        ret,thresh = cv2.threshold(gray,127,255,0)
        if '3.4.2' == cv2_version :
            contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            cv2.drawContours(gray, contours, -1, (0,255,0), 3)
        
        else:
            contours, hierarchy, more = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            cv2.drawContours(gray, contours, -1, (0,255,0), 3)
        cv2.imshow('Contours', gray)
        
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    cap.release()
    cv2.destroyAllWindows()
        
    
