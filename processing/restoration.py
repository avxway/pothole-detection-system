import cv2

def restore(image):
    return cv2.GaussianBlur(image,(5,5),0)
