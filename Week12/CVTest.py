import cv2

path = r"C:\Users\tobin\Documents\_Repos\CSC-106\Week12\box1.jpg"
print(path)
image = cv2.imread(path)

cv2.imshow(":)", image)

cv2.waitKey(0)