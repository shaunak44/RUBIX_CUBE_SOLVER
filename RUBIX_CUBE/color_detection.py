import cv2
import numpy as np
video_capture = cv2.VideoCapture(0)
def Draw_rectangle(x1, y1, x2, y2) :
    roi = frame[y1:y2, x1:x2]
    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
    #cv2.imshow('ROI', roi)
    return roi
def nothing(x) :
    pass
cv2.namedWindow('Threshold')
hmax = 'hmax'
hmin = 'hmin'
smax = 'smax'
smin = 'smin'
vmax = 'vmax'
vmin = 'vmin'
cv2.createTrackbar("hmax", "Threshold", 0, 255, nothing)
cv2.createTrackbar("hmin", "Threshold", 0, 255, nothing)
cv2.createTrackbar("smax", "Threshold", 0, 255, nothing)
cv2.createTrackbar("smin", "Threshold", 0, 255, nothing)
cv2.createTrackbar("vmax", "Threshold", 0, 255, nothing)
cv2.createTrackbar("vmin", "Threshold", 0, 255, nothing)
green = np.uint8([[[0,0,255]]])
hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
print( hsv_green )
while(1) :
    hmax = cv2.getTrackbarPos("hmax", "Threshold")
    hmin = cv2.getTrackbarPos("hmin", "Threshold")
    smax = cv2.getTrackbarPos("smax", "Threshold")
    smin = cv2.getTrackbarPos("smin", "Threshold")
    vmax = cv2.getTrackbarPos("vmax", "Threshold")
    vmin = cv2.getTrackbarPos("vmin", "Threshold")
    ret, frame = video_capture.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    RED = cv2.inRange(hsv, (hmin, smin, vmin), (hmax, smax, vmax))
    #RED = cv2.inRange(hsv, (0, 0, 0), (173, 255, 255))
    #YELLOW = cv2.inRange(hsv, (25, 155, 50), (35, 255,255))
    #GREEN = cv2.inRange(hsv, (26,255 ,50 ), (145,255,147))
    #BLUE = cv2.inRange(hsv, (98, 118, 106), (160, 255, 255))
    #WHITE = cv2.inRange(hsv, (5,0,136 ) ,(128, 77,213))
    #ORANGE = cv2.inRange(hsv, (0, 193, 128), (4, 255, 255))
    #ret, frame = video_capture.read()
    #roi = frame[50:100, 200:250]
    #cv2.rectangle(frame, (200,50), (250, 100), (255, 0, 0), 2)
    #cv2.imshow('ROI', roi)
    roi1 = Draw_rectangle(200, 50, 250, 100)
    roi2 = Draw_rectangle(250, 50, 300, 100) 
    roi3 = Draw_rectangle(300, 50, 350, 100) 
    roi4 = Draw_rectangle(200, 100, 250, 150)
    roi5 = Draw_rectangle(250, 100, 300, 150) 
    roi6 = Draw_rectangle(300, 100, 350, 150)
    roi7 = Draw_rectangle(200, 150, 250, 200)
    roi8 = Draw_rectangle(250, 150, 300, 200) 
    roi9 = Draw_rectangle(300, 150, 350, 200) 
    cv2.imshow('Video', frame)
    cv2.imshow('RED', RED)
    #cv2.imshow('YELLOW', YELLOW)
    #cv2.imshow('GREEN', GREEN)
    #cv2.imshow('BLUE', BLUE)
    #cv2.imshow('ORANGE', ORANGE)
    #cv2.imshow('WHITE', WHITE)
    if(cv2.waitKey(1) & 0xFF == ord('q')) :
        break
video_capture.release()
cv2.destroyAllWindows()
