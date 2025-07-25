import cv2
import numpy as np
image = cv2.imread('images/chevy.png')
cv2.rectangle(image, (1000, 500), (80, 210), (0, 0, 255), 4)
cv2.putText(image, 'Chevy', (250, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
cv2.imshow('Chevrolet',image)
cv2.waitKey(0)
