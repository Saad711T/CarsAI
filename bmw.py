import cv2
import numpy as np
image = cv2.imread('images/bmw.png')
cv2.rectangle(image, (1000, 500), (200, 200), (255, 50, 50), 4)
cv2.putText(image, 'BMW', (250, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 50, 50), 2)
cv2.imshow('BMW',image)
cv2.waitKey(0)
