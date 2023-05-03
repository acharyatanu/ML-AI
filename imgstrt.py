#to have a gray cale img (img_gray)and black and white (img_bw)
import cv2
vid=cv2.VideoCapture(0)
while True:                              #to have infinte loop
    flag,img=vid.read()
    if flag:
        #Processing code
        img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        th,img_bw=cv2.threshold(img_gray,100,255,cv2.THRESH_BINARY)

        #print(type(img_gray))
        #break
        ##
        cv2.imshow('preview',img_bw)
        key=cv2.waitKey(1)
        if key==ord('a'):                 #ASCII value of a is given to key
            break
    else:
          break                           #if camera is not captured than also break
vid.release()
cv2.destroyAllWindows()