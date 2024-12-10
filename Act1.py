import cv2 

img=cv2.imread("Gohan.jpg")
cv2.imshow("Original",img) 

gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("GrayScale",gray_image)

cv2.waitKey(0)
cv2.destroyAllWindows()