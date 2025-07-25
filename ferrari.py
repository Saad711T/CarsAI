import cv2
import numpy as np
image = cv2.imread('images/ferrari.png')
cv2.rectangle(image, (1100, 500), (150, 200), (150, 150, 50), 4)
cv2.putText(image, 'Ferrari', (280, 240), cv2.FONT_HERSHEY_SIMPLEX, 1, (150, 150, 50), 2)
cv2.imshow('Ferrari',image)
cv2.waitKey(0)
