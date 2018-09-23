import cv2
import numpy as np
import platform
import threading
import time
from matplotlib import pyplot as plt


def main(args):
    print("OS Version:", platform.release() )
    print("Starting... ", time.clock())
    
    
def two2one(img1, img2 , size1, size2):
    img3=img1.copy()
    img3=cv2.resize(img3, (0,0), None, 0.25, 0.25)
    
    
    pass

    
if __name__ == '__main__':
    import sys
    main(sys.argv[1:]) 
    bits = 0xA355
    pp0 = cv2.imread('yellow-ping-pong.png')
    pp2 = cv2.cvtColor(pp0, cv2.COLOR_BGR2GRAY)
    
    www = list(pp2.shape[::-1])
    print (www)
    wp = www[0]
    hp = www[1]
    orb = cv2.ORB_create()
    
    cv2_version = cv2.__version__
    print ("OpenCV version:", cv2.__version__)
    #kpPP, desPP = orb.detectAndCompute(pingPong, None)
    cap = cv2.VideoCapture(0)
    methods = [ 'cv2.TM_CCOEFF',       'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
                'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF',        'cv2.TM_SQDIFF_NORMED']


    #while(True):
    ret , frame = cap.read()
    pp3 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    
    www = list( pp3.shape[::-1] ) 
        
    w = www[0]
    h = www[1]
    
    www = list( pp3.shape[::-1] ) 
        
    w = www[0]
    h = www[1]
    
    #print (w, h, cv2.CV_8U, cv2.CV_32F)
    for meth in methods:
            
            method= eval(meth)
            frame = pp3.astype(np.float32)
            res = cv2.matchTemplate(pp3, pp2, method )
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED ]:
                top_left = min_loc
            else:
                top_left = max_loc
            
            bottom_right = (top_left[0]+ w, top_left[1]+ h)
          
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            vis = np.concatenate((pp2, res, frame), axis=0)
            cv2.imshow(vis, "")
            if cv2.waitKey(1) & 0xFF == ord('q'):
                pass
             
    cap.release()
    cv2.destroyAllWindows()
    