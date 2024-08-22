import cv2
import numpy as np
import imutils

# Зчитування та відображення зображення, збереження
img_path = '/Users/jperv/PycharmProjects/LAB1AI/hosion_moment.jpg'
img = cv2.imread(img_path)
img_gray = cv2.imread(img_path,0)
cv2.imshow('Original', img)
cv2.imshow('Gray', img_gray)
cv2.imwrite('/Users/jperv/PycharmProjects/LAB1AI/hosion_gray.jpg', img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Зміна розміру зображення
resized = imutils.resize(img_gray, width=400)

h, w = img.shape[0:2]
h_new = 400
ratio = w / h
w_new = int(h_new * ratio)
resized_2 = cv2.resize(img, (w_new, h_new))

cv2.imshow('resized with imutils', resized)
cv2.imshow('resized with cv2', resized_2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Розмите та повернутезображення
h, w = resized_2.shape[0:2]
center = (w // 2, h // 2)
rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated_cv2 = cv2.warpAffine(resized_2, rotation_matrix, (w, h))

rotated_imutils = imutils.rotate(resized, -45)

blurred = cv2.GaussianBlur(rotated_imutils,(11,11),0)

cv2.imshow('Rotated image with cv2', rotated_cv2)
cv2.imshow('Rotated and blurred image with imutils', blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Зклейка зображень
suming = np.hstack((resized, blurred))
cv2.imshow('Summed', suming)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Bирізання зображення + текст
roi = img[130:450,450: 850]
font = cv2.FONT_ITALIC
cv2.putText(roi, 'WoT enjoyers', (0, 50), font,2,(0,0,255),2,cv2.LINE_AA)

cv2.imshow('ROI', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Трикутник, лінія, квадрат, коло
img_black = np.zeros((400, 400, 3), np.uint8)
cv2.circle(img_black, (200,238), 57, (255,255,255),4)
cv2.rectangle(img_black, (100,100), (300,300), (255,255,255), 2)
cv2.line(img_black, (200,100), (200,300), (255,255,255), 4)
points = np.array([[200,100],[100,300],[300,300],[200,100]])
cv2.polylines(img_black, np.int32([points]), 1, (255,255,255),4)
cv2.imshow('Figures', img_black)
cv2.waitKey(0)
cv2.destroyAllWindows()
