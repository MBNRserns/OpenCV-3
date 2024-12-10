import cv2

img=cv2.imread("Gohan.jpg")
cv2.imshow("Original",img)

#setting parameter values
t_lower = 50 #lower threshold
t_upper = 250 #upper threshold

#applying the Canny Edge filter
edge=cv2.Canny(img,t_lower,t_upper)
cv2.imshow("Canny Edge",edge)

cv2.waitKey(0)
cv2.destroyAllWindows()