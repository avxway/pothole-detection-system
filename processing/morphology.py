import cv2
import numpy as np

def apply_morphology(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((5,5),np.uint8)
    return cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
