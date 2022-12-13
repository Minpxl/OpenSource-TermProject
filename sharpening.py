import cv2
import math

src=cv2.imread('c:/image/road.jpg')
if src is None:
    print('Image load failed')
    sys.exit()

gray=cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(src, 100, 255)


cv2.imshow("canny",canny)
cv2.waitKey()
cv2.destroyAllWindows()
