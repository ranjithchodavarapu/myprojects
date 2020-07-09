import cv2
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img=cv2.imread(r'C:\Users\Ranjith ch\Desktop\sus.jpg')
img=cv2.resize(img,(500,500))
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray,1.1,4)
for(x,y,w,h)in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
cv2.imshow('image',img)
cv2.waitKey()