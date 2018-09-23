import cv2
import numpy as np
from matplotlib import pyplot as plt
name1='stop_sign.png'

name3 ='stop1.jpg'

name2='to_find2.jpg'

p1 = cv2.imread(name3)
p2 = cv2.imread(name2)


orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(p1, None)
kp2, des2 = orb.detectAndCompute(p2, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck= True)

matches = bf.match(des1, des2)

matches = sorted(matches, key = lambda x:x.distance)

matching_result = cv2.drawMatches(p1, kp1, p2, kp2, matches[:40] , None, flags=2)

#cv2.imshow("1", p1)
#cv2.imshow("2", p2)
cv2.imshow("R", matching_result)
cv2.waitKey(0)
cv2.destroyAllWindows()


