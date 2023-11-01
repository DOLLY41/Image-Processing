import cv2
import matplotlib.pyplot as plt

img = cv2.imread('C:/Users/ADITYA/OneDrive/DOLLY/dolly/OneDrive/Pictures/Saved Pictures/C3aVXGMXUAETfYA.jpg')
cv2.imshow('IMAGE', img)
plt.imshow(img)
plt.show()

img2 = img.copy()
img2[100:200, 100:300] = 0
plt.imshow(img2, cmap='gray')
plt.show()

img2[300:400, 400:600] = 255
plt.imshow(img2, cmap='gray')
plt.show()
