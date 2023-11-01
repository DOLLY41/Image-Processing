#There are  5 library which is used for image processing
from skimage import io
img1 = io.imread('C:/Users/ADITYA/OneDrive/DOLLY/dolly/OneDrive/Pictures/Saved Pictures/C3aVXGMXUAETfYA.jpg')

import cv2
img2 = cv2.imread('C:/Users/ADITYA/OneDrive/DOLLY/dolly/OneDrive/Pictures/Saved Pictures/C3aVXGMXUAETfYA.jpg')
cv2.imshow('PICTURE',img2)
import numpy as np
a= np.ones((5,5))

from matplotlib import pyplot as plt
plt.imshow(img1)
plt.show()
plt.imshow(a,cmap='BrBG')
plt.show()
