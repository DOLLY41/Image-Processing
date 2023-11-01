import cv2
import numpy as np
import matplotlib.pyplot as plt

img = np.arange(6)
img = img[np.newaxis, :]
img = np.repeat(img, 10, axis=0)
print(img)
plt.imshow(img,cmap='gray')
plt.show()
