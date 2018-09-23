import cv2
import numpy as np
import sys
from matplotlib import pyplot as plt
name1='pp1.jpg'

name3 ='stop1.jpg'

name2 = 'to_find2.jpg'
name4 = 'yellow_ping_pong.png'
name5 = 'logo1.jpg'
name6 = 'logo2.jpg'
name7 = 'logo3.jpg'
name8 = 'logo4.jpg'
name9 = 'logo5.jpg'
name10 = 'logo6.jpg'
name11 = 'comp1.jpg'
names = [name1, name2, name3, name4, name5, name6, name7, name8, name9, name10, name11]

name = names[int(sys.argv[2])]
print("Using file ", name)

p1 = cv2.imread(name)
p1 = cv2.cvtColor(p1, cv2.COLOR_BGR2HSV)
orb = cv2.ORB_create()
cap = cv2.VideoCapture(0)

to_match =int(sys.argv[1])


while True:
    ret, p2 = cap.read()
    p2 = cv2.cvtColor(p2, cv2.COLOR_BGR2HSV)
    kp1, des1 = orb.detectAndCompute(p1, None) 
    kp2, des2 = orb.detectAndCompute(p2, None)
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck= False)
    matches = bf.match(des1, des2
                       #, k=2
                       )
    
    #matches = sorted(matches, key = lambda x:x.distance)
    
    matchesMask = [[0,0] for i in range(len(matches))]
    #for i, (m,n) in enumerate(matches):True
    #    if 0.55*n.distance < m.distance < 0.80*n.distance :
    #        matchesMask[i]= [1, 0]True
    #        draw_params = dict(matchesMask = matchesMask)
    print("Matched ", len(matches) )
    
    matching_result = cv2.drawMatches(p1, kp1, p2, kp2, matches[:to_match] , None, flags=2)
    m1 = matching_result[:1]
    
    print(m1, type(m1), m1.data, m1.dtype, m1.nbytes, m1.ndim, m1.shape, m1.flags)
#cv2.imshow("1", p1)
#cv2.imshow("2", p2)
    cv2.imshow("R", matching_result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()        
cv2.destroyAllWindows()


