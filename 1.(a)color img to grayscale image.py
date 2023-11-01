#COLOR IMAGE TO GRAY SCALE IMAGE
import cv2
img= cv2.imread('C:/Users/ADITYA/OneDrive/DOLLY/dolly/OneDrive/Pictures/Saved Pictures/Data-Science-course-Computer-Science-Certification-Courses.jpg')
gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('IMAGE1',img)
cv2.imshow('IMAGE',gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
