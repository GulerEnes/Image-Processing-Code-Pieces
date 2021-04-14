import numpy as np
import cv2

#img = cv2.imread('lena.jpg', 1)
img = np.zeros([512, 512, 3], np.uint8) # this creates a black image with our width height sizes

img = cv2.line(img, (30, 30), (100, 100), (255, 0, 0), 5)  # it is using to draw a line on img
# parameter of this: img, starting point, ending point, bgr color code, thickness
img = cv2.arrowedLine(img, (50, 30), (100, 100), (0, 255, 0), 5)
# there are some other funcs as rectangle, circle...

font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'OpenCV', (200, 200), font, 1, (0, 0, 255), 3, cv2.LINE_AA)  # To write something on img
# parameters are: img, text, starting point, font(from cv2 framework), font size,color(bgr form), thickness, line type

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()




