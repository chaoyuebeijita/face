import cv2
import numpy as np
#from scipy.misc import imread, imresize,imshow

img = cv2.imread("C:\lena.jpg")
cv2.imshow('image',img)
cv2.waitKey(10000)
