import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
img = cv2.imread('family.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faceDetected = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x, y, w, h) in faceDetected:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    blurred = img[y:y+h, x:x+w]
    blurred = cv2.blur(blurred,(50,50))
    imgBlurred = img
    imgBlurred[y:y+h, x:x+w] = blurred

cv2.imshow('result', img)

cv2.waitKey(0)
cv2.destroyAllWindows()