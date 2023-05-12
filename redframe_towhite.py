import cv2
from time import sleep


vid= cv2.VideoCapture(0)
while True:
    flag, img = vid.read()
    if(flag):
        img=cv2.convertScaleAbs(img,beta=10,alpha=1.5)
        red_plane = img[:,:,-1].copy()
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        red_img = cv2.subtract(red_plane,gray_img)
        th,red_binary=cv2.threshold(red_img,48,255,cv2.THRESH_BINARY)
        cv2.imshow('Preview',red_binary)
        key= cv2.waitKey(1)
        if key == ord('a'):
            break
    else:
        print('No Frames')
        break
    sleep(0.1)

cv2.destroyALlWindows()        
cv2.waitKey(1)
vid.release()