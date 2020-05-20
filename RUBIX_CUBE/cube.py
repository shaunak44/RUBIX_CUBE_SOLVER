import cv2
import numpy as np

def Draw_rectangle(x1, y1, x2, y2) :
    roi = frame[y1:y2, x1:x2]
    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
    #cv2.imshow('ROI', roi)
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV) 
    return roi

def nothing(x) :
    pass

def average_hsv(roi):
        """ Average the HSV colors in a region of interest.

        :param roi: the image array
        :returns: tuple
        """
        h   = 0
        s   = 0
        v   = 0
        num = 0
        for y in range(len(roi)):
            for x in range(len(roi[y])):
                chunk = roi[y][x]
                num += 1
                h += chunk[0]
                s += chunk[1]
                v += chunk[2]

        h = h / num
        s = s / num
        v = v / num
        return (int(h), int(s), int(v))

def get_color_name(hsv):
        """ Get the name of the color based on the hue.

        :returns: string
        """
        (h,s,v) = hsv
        print((h,s,v))
        if h >= 52 and h <= 70 :
            return 'green'
        elif h >= 100 and h <= 130:
            return 'blue'
        elif h <= 45:
            return 'orange'
        elif h >= 150:
            return 'red'
        elif h >= 46 :
            return 'yellow'
        else :
            return 'white'
        """if h <= 4 and v > 128 and s > 193:
            return 'orange'
        elif h > 5 and s <= 77 and h < 128 and v < 213 and v > 136:
            return 'white'
        elif h > 25 and h <= 35 and s > 155 and v > 50:
            return 'yellow'
        elif h > 26 and h < 145 and s > 253 and v > 50 and v < 147:
            return 'green'
        elif h <= 160 and h > 98 and s > 118 and v > 106:
            return 'blue'

        return 'red'"""


side =[]
video_capture = cv2.VideoCapture(0)

while(1) :

    ret, frame = video_capture.read()
    #hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
 
    #RED = cv2.inRange(hsv, (0, 0, 0), (173, 255, 255))
    #YELLOW = cv2.inRange(hsv, (25, 155, 50), (35, 255,255))
    #GREEN = cv2.inRange(hsv, (26,255 ,50 ), (145,255,147))
    #BLUE = cv2.inRange(hsv, (98, 118, 106), (160, 255, 255))
    #WHITE = cv2.inRange(hsv, (5,0,136 ) ,(128, 77,213))
    #ORANGE = cv2.inRange(hsv, (0, 193, 128), (4, 255, 255))  
   
   
    one = Draw_rectangle(210, 100, 235, 125)
    two = Draw_rectangle(280, 100, 305, 125)
    three = Draw_rectangle(350, 100, 375, 125)
    four = Draw_rectangle(210, 170, 235, 195)
    five = Draw_rectangle(280, 170, 305, 195)
    six = Draw_rectangle(350, 170, 375, 195)
    seven = Draw_rectangle(210, 240, 235, 265)
    eight = Draw_rectangle(280, 240, 305, 265)
    nine = Draw_rectangle(350, 240, 375, 265)

  #  contours,_ = cv2.findContours(BLUE, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  #  for cnt in contours :
  #      area = cv2.contourArea(cnt)
  #      if(area > 3000):
  #         print("BLUE DETECTED")
  #         cv2.imshow('BLUE',BLUE)
    cv2.imshow('Video', frame)
    if(cv2.waitKey(10) & 0xFF == 32) :  #for space ascii
        side.append(one)
        side.append(two)
        side.append(three)
        side.append(four)
        side.append(five)
        side.append(six)
        side.append(seven)
        side.append(eight)
        side.append(nine)
        print("Side saved")

    #if(cv2.waitKey(1) & 0xFF == 27) : #for escape ascii
     #   break
    if(cv2.waitKey(1) & 0xFF == ord('q')) :
        break



print("The color is :")
avg = average_hsv(side[0])
color = get_color_name(avg)
print(color)
video_capture.release()
cv2.destroyAllWindows()
