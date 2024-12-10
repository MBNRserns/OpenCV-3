import cv2

img=cv2.imread("Gohan.jpg")
cv2.imshow("Original",img)

hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow("HSV",hsv)

cv2.waitKey(0)
cv2.destroyAllWindows()