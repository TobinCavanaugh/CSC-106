import cv2
import numpy as np

img1 = cv2.imread(r"C:\Users\tobin\Documents\_Repos\CSC-106\Week13\clarke.png")
img2 = cv2.imread(r"C:\Users\tobin\Documents\_Repos\CSC-106\Week13\clarke-1.png")

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

def mse(img1, img2):
    h, w = img1.shape
    diff = cv2.subtract(img1, img2)
    err = np.sum(diff ** 2)
    mse = err / (float(h * w))
    return mse, diff

error, diff = mse(img1, img2)
print(error, diff)