import cv2

img = cv2.imread('family.png')
blurred = cv2.blur(img,(50,50))

cv2.imshow('result', blurred)

cv2.waitKey(0)
cv2.destroyAllWindows()