Detects Faces with blurred status using cascade.

This project consists of the following steps:
1. Find the image named family
2. Define 'blurred' to use 
3. Capture faces from the picture
4. Make faces blurred which we defined 

## Methods
- cv2.imread(), cv2.waitkey(), cv2.destroyAllWindows() 
- cv2.CascadeClassifier: It is a progress of stepping to exclude which is not a face by using features of darkness.  
- cv2.Cascade.detectMultiScale: Read and detect the object by using the data which was stored before. 
- Haarcascade_frontalface_default.xml: Detect the face of front

## Version
python 3.10.6, Opencv 4.6.0

## Results
- face detected
![img_face](https://user-images.githubusercontent.com/106726948/207326820-f0668984-d0e4-4aa0-a9d8-96f128ad57ae.png)
- blurred
![img_blurred](https://user-images.githubusercontent.com/106726948/207326890-f5a5def5-57cd-49b0-b942-0cf934b24736.png)
- face detected & blurred
![img_blurredface](https://user-images.githubusercontent.com/106726948/207326759-22e958fb-cbad-4020-8887-dfa1445de86b.png)

 * If the face is hidden, it can't be detected. 

## Reference
- https://blog.naver.com/playonu/222702485973
- https://github.com/opencv/opencv/tree/master/data/haarcascades