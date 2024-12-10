import cv2

img=cv2.imread("Gohan.jpg")
cv2.imshow("Original",img)

rotate_img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("Rotated", rotate_img)

rotate_img1 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow("Rotated left", rotate_img1)

rotate_img2 = cv2.rotate(img,cv2.ROTATE_180)
cv2.imshow("Upside down", rotate_img2)

cv2.waitKey(0)
cv2.destroyAllWindows()