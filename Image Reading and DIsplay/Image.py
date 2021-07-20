import cv2 as cv
import sys

img = cv.imread("/home/lajith/Downloads/ViratKohli.jpg")

if img is None:
	sys.exit("Could not read the image")

cv.imshow("Virat Kohli",img)
k=cv.waitKey(0)

if k==ord("s"):
	cv.imwrite("ViratKohli.jpg")