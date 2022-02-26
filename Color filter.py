#Color filter session 1 and 2 .
import numpy as np
import itertools
import cv2
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import glob
import os
import pandas as pd
import openpyxl
import sys
# reading excle
#useless for our first scenario but it would be useful for our second scenario.
#read from excel
df = pd.read_excel('C:/Users/asus/Desktop/Barcodes.xlsx')

#insert a coulmn in df
color_code_list = []
for i in range(0, 81):color_code_list.append([0.,0.,0.])    
df.insert(1,"colors_code",color_code_list)

# Input glasses code from site
Barcode=input("please enter sunglsses barcode: ")
cv_img = plt.imread('C:/Users/asus/Desktop/05/COLORS/'+ Barcode +'.jpg')    
cv_img = cv_img.copy()
cv_img = cv_img.astype("int")
plt.imshow(cv_img)

# input picture from customer and adding more contrast
#have to find the code for getting an input image from user
#or maybe it's for backend coding part!!!
customer_img = plt.imread('C:/Users/asus/Desktop/05/CUSTOMER/Co.jpg')
customer_img = customer_img.copy()
customer_img = customer_img.astype("int")
contrast = 40

img_con = customer_img * (contrast/127 + 1 ) - contrast
img_con = np.clip(img_con, 0, 255)
img_con = img_con.astype("uint8")
plt.imshow(img_con)

# FILTER CODE
# just blending two imgs
img_blend = cv_img*0.3 + img_con* 0.7
img_blend = np.clip(img_blend, 0, 255)
img_blend = img_blend.astype("uint8")
plt.imshow(img_blend)

# save img at new location
#save 
im_rgb = cv2.cvtColor(img_blend, cv2.COLOR_BGR2RGB)
save = cv2.imwrite('C:/Users/asus/Desktop/best.jpg',im_rgb)
#Done 