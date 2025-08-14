import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
current_dir=os.path.dirname(__file__)
img_path=os.path.join(current_dir,"Bird.jpeg")
img=cv2.imread(img_path,cv2.IMREAD_COLOR)
rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#resizing before display
cv2.namedWindow("RGB",cv2.WINDOW_NORMAL)
cv2.imshow("RGB",rgb)
cv2.resizeWindow("RGB",800,600)
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.namedWindow("HSV",cv2.WINDOW_NORMAL)
cv2.imshow("HSV",hsv)
cv2.resizeWindow("HSV",800,600)
lab=cv2.cvtColor(img,cv2.COLOR_BGR2LAB)
cv2.namedWindow("LAB",cv2.WINDOW_NORMAL)
cv2.imshow("LAB",lab)
cv2.resizeWindow("LAB",800,600)
cv2.namedWindow("Org",cv2.WINDOW_NORMAL)
cv2.imshow("Org",img)
cv2.resizeWindow("Org",800,600)
#identifying red color
#red appears twice at low(0-10) and at high(170-180) hue values
lower_red1=np.array([0,120,70])
upper_red1=np.array([10,255,255])
lower_red2=np.array([170,120,70])
upper_red2=np.array([180,255,255])
mask1=cv2.inRange(hsv,lower_red1,upper_red1)
mask2=cv2.inRange(hsv,lower_red2,upper_red2)
red_mask=cv2.bitwise_or(mask1,mask2)
red_areas=cv2.bitwise_and(img,img,mask=red_mask)
#resizing before display
scale_percent=30  # shrink to 30%
width=int(img.shape[1]*scale_percent / 100)
height=int(img.shape[0]*scale_percent / 100)
mask1_small=cv2.resize(mask1,(width, height))
mask2_small=cv2.resize(mask2,(width, height))
red_mask_small=cv2.resize(red_mask,(width, height))
red_areas_small=cv2.resize(red_areas,(width, height))
cv2.imshow("Mask 1",mask1_small)
cv2.imshow("Mask 2",mask2_small)
cv2.imshow("Red mask",red_mask_small)
cv2.imshow("Red areas",red_areas_small)
cv2.waitKey(0)
cv2.destroyAllWindows()

