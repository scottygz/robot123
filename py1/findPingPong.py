import cv2
import numpy as np
import platform
import threading
import time
from matplotlib import pyplot as plt


def main(args):
    print("OS Version:", platform.release() )
    print("Starting... ", time.clock())
    
    
    
if __name__ == '__main__':
    import sys
    main(sys.argv[1:]) 
    bits = 0xA355
    pingPong = cv2.imread('yellow-ping-pong.png', 0 )
    orb = cv2.ORB_create()
    
    
    
    cv2_version = cv2.__version__
    print ("OpenCV version:", cv2.__version__)
    kpPP, desPP = orb.detectAndCompute(pingPong, None)
    cap = cv2.VideoCapture(0)
    
    while(True):
        ret , frame = cap.read()
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        kp2, des2 = orb.detectAndCompute(frame, None)
        
        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)
        
        matches = bf.match(desPP, des2)
        
        matches = sorted(matches, key = lambda x:x.distance)
        img3 = None
        img3 = cv2.drawMatches(pingPong, keypoints1=kpPP, outImg=img3, img2=frame, keypoints2=kp2, matches1to2=matches[0:10])
        
        cv2.imshow('Found', img3)
        
        
        
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    cap.release()
    cv2.destroyAllWindows()
    
        