import cv2
import plotly
import plotly.express as px
import skimage

vid=cv2.VideoCapture(0)
while True:


#img=skimage.data.astronaut()                                               #RGB
 flag,img=vid.read()
 img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
 if flag:
    img_p=cv2.subtract(img[:,:,-1],cv2.cvtColor(img,cv2.COLOR_RGB2GRAY))       #blue area highlighted with white and rest is black
    th,img_p2=cv2.threshold(img_p,60,255,cv2.THRESH_BINARY)                    #to get a pure binary image
    img_p3=skimage.morphology.remove_small_objects(img_p2.astype(bool),50)     #skimage use bool value for morphology so we astype the img_p2,morphology will see for continuous 50m pixel together and removeall othe rwhite pixels
    img_p4=cv2.dilate(img_p3.astype('uint8'),cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(10,10))).astype(bool)    #we have to use dialation approach here as no proper hole ids there in the badge img
    img_p5=skimage.morphology.remove_small_holes(img_p4,2000)   
    rp=skimage.measure.regionprops(skimage.measure.label(img_p5)) 
    img_preview=img.copy()                          #will give the region of the highligted image
    if len(rp)>0:
        (y1,x1,y2,x2)=rp[0].bbox
        cv2.rectangle(img_preview,pt1=(x1,y1),pt2=(x2,y2),color=(255,255,0),thickness=3)

 #imshowPx(img_preview,cv=False,gray=True)
        cv2.imshow('Preview',img_preview[:,:,::-1])
        key=cv2.waitKey(1)
        if key == ord('a'):
            break
cv2.destroyALlWindows()        
cv2.waitKey(1)
vid.release()