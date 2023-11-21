import numpy as py
import cv2 as cv

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Exiting")
        break

    color = cv.cvtColor(frame, cv.COLOR_RGB2RGBA)
    
    cv.imshow('frame', color)

    if(cv.waitKey(1) == ord('q')):
        break

cap.release()
cv.destroyAllWindows()