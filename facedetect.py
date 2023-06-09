#to detect face 

import cv2
from time import sleep
import numpy as np

fd=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
vid=cv2.VideoCapture(0)
while True:                              #to have infinte loop
    flag,img=vid.read()
    if flag:
        #Processing code
        img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=fd.detectMultiScale(img_gray,
                                  scaleFactor=1.1,
                                  minNeighbors=5,
                                  minSize=(50,50)
                                  )
        np.random.seed(50)
        colors=np.random.randint(0,255,(len(faces),3)).tolist()   #this can also be used :-   colors=[np.random.randint(0,255,3).tolist() for i in faces]
        i=0
        # th,img_bw=cv2.threshold(img_gray,100,255,cv2.THRESH_BINARY_INV)
        for x,y,w,h in faces:
         #x,y,w,h=(250,200,100,100)
         #img_cropped =img[y:y+h,x:x+w,:]
         cv2.rectangle(img,pt1=(x,y),pt2=(x+w,y+h),color=colors[i],thickness=2)
         i+=1

        #print(type(img_gray))
        #break
        ##
        cv2.imshow('preview',img)
        key=cv2.waitKey(1)
        if key==ord('a'):                 #ASCII value of a is given to key
            break
    else:
       print('No Frames')
       break 
    sleep(0.1)                          #if camera is not captured than also break
vid.release()
cv2.destroyAllWindows()