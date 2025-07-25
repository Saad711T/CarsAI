import cv2
import numpy as np
image = cv2.imread('images/ford.png')
cv2.rectangle(image, (1000, 700), (70, 400), (40, 90, 40), 4)
cv2.putText(image, 'Ford', (430, 455), cv2.FONT_HERSHEY_SIMPLEX, 1, (40, 90, 40), 2)
cv2.imshow('Ford',image)
cv2.waitKey(0)