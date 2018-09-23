import cv2
import numpy as np
from matplotlib import pyplot as plt
name1='stop_sign.png'
name3 ='stop1.jpg'
name2='to_find2.jpg'
n1 = name3
n2 = name2

template = cv2.imread( n1, 0 )
w, h = template.shape[::-1]
#template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
template = template.astype(np.float32)

# All the 6 methods for comparison in a list
#methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
#            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

#cap = cv2.VideoCapture(0)
img =cv2.imread(n2)
img2 = img.copy()

   
#for meth in methods:
img = img2.copy()
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = img.astype(np.float32)

res = cv2.matchTemplate(img,template, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
threshold = 0.8
loc = np.where(res >= threshold )
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, ( pt[0]+w, pt[1]+h ), (0,0,255), 2)

cv2.imshow('source', img)
cv2.waitKey(0)    

    
    