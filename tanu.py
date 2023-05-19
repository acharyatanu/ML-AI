import cv2
import face_recognition as fr
import pandas as pd

fd=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

vid=cv2.VideoCapture(0)
name=input('enter your name:')
frameCount=0
frameLimit=20
names=[]
enc=[]
while True:
    flag,img=vid.read()
    if flag:
            img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces=fd.detectMultiScale(img_gray,
                                  scaleFactor=1.1,
                                  minNeighbors=5,
                                  minSize=(50,50)
                                  )
            if len(faces)==1:
                x,y,w,h=faces[0]
                img_face=img[y:y+h,x:x+w,:].copy()
                img_face=cv2.resize(img_face,(400,400),cv2.INTER_CUBIC)
                face_encoding=fr.face_encodings(img_face)
                if len(face_encoding==1):
                    enc.append(face_encoding[0])
                    names.append(name)
                    frameCount+=1
                    if frameCount ==frameLimit:
                        break
    
            
            for x,y,w,h in faces:
                cv2.rectangle(img,pt1=(x,y),pt2=(x+w,y+h),color=(0,0,255),thickness=3)

            cv2.imshow('preview',img)
            key=cv2.waitKey(1)
            if key==ord('a'):                 #ASCII value of a is given to key
                break
data={'names':names,'encoding':enc}
pd.DataFrame(data).to_csv('face_data.csv')
cv2.destroyAllWindows()
cv2.waitKey(1)
vid.release()
            