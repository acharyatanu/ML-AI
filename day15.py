import cv2
import plotly
import plotly.express as px
import skimage
def imshowPx(im,cv=True,gray=False):
    fig=px.imshow(im[:,:,::-1] if cv else im,binary_string=gray)
    fig.update_xaxes(visible=False)         #to hide the x axis coordinate
    fig.update_yaxes(visible=False)         #to hide y axes coosdinate
    plotly.io.show(fig)

img=skimage.data.astronaut()      #RGB
img_p=cv2.subtract(img[:,:,-1],cv2.cvtColor(img,cv2.COLOR_RGB2GRAY))
imshowPx(img_p,cv=False,gray=True)
