import cv2
import numpy as np

src=cv2.imread('c:/image/road.jpg')
if src is None:
    print('Image load failed')
    sys.exit()

gray=cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
sharp = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

sharpening = cv2.filter2D(gray, -1, sharp)

cv2.imshow('sharpening2', sharpening)
cv2.waitKey()
cv2.destroyAllWindows()
