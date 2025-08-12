import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
current_dir=os.path.dirname(__file__)
img_path=os.path.join(current_dir,"Swathi.jpg")
img=cv2.imread(img_path,cv2.IMREAD_UNCHANGED)
'''cv2.imread(path,flags) where flags can be cv2.IMREAD_COLOR(BGR)
or cv2.IMREAD_GRAYSCALE(loads in grayscale)
or cv2.IMREAD_UNCHANGED (includes alpha transparency channel if present)'''
#alpha transparency refers to opacity or transparency, 0-> fully transparent, 255-> fully opaque
#if transparency is present img.shape will give output of 4 for hannels instead of 3
if img is None:
    print("Image not found")
    exit()
cv2.imshow('Image',img)
#Alternate method to display using matplotlib
img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #matplotlib expects images in RGB format
plt.imshow(img_rgb)
plt.title("My image")
plt.axis('off') #hide axis
plt.show()

#Loading and exploring pixels
print("Height, Width and Channels= ",img.shape)
height,width,channels=img.shape
print(f"Height: {height}")
print(f"Width: {width}")
print(f"Channels: {channels}")
print("Datatype: ",img.dtype)
print("Total pixels: ",img.size) #-->total no of values=height*width*channel

#whenever we access an image's pixels with its index, img[y,x]

#Accessing pixel values
px=img[50,100]
print("Pixel values at (100,50): ",px)
        #to visualise this pixel
color_patch=np.zeros((100,100,3),dtype=np.uint8)
color_patch[:]=[px[0],px[1],px[2]]
cv2.imshow("Color at px",color_patch)
blue=img[50,100,0]
print("Blue value at px: ",blue)

#modifying pixel values
img[50,100]=[0,0,255]
img[51,100]=[0,0,255]
img[52,100]=[0,0,255]
img[53,100]=[0,0,255]
img[54,100]=[0,0,255]
img[55,100]=[0,0,255]
img[56,100]=[0,0,255]
img[57,100]=[0,0,255]
img[58,100]=[0,0,255]
img[59,100]=[0,0,255]
img[60,100]=[0,0,255]
cv2.imshow("Modified pixels",img)

#splitting and merging channels
b,g,r=cv2.split(img)
cv2.imshow("Blue channel",b)
cv2.imshow("Green channel",g)
cv2.imshow("Red channel",r)
merged=cv2.merge([b,g,r])
cv2.imshow("Merged channels",merged)
cv2.waitKey(0)
cv2.destroyAllWindows()
