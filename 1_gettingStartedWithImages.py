import cv2

img = cv2.imread('lena.jpg', -1) # Second parameter of this func is specifies the way image should be read
                            # It can be 1,0,-1 respectively cv2.IMREAD_COLOR, cv2.IMREAD_GRAYSCALE,cvIMREAD_UNCHANGED
                            # Which are respectively LOads a color image, Loads image in grayscale mode,
                            # Loads image as such including alpha channel


#print(img) # it prints the image matrix

cv2.imshow('image', img) # it shows the image. First parameter is just window name which is unimportant

k = cv2.waitKey(0)# to avoid the automatically closing window we use this func to keep img for x milisecond
                  # If you give 0 as parameter image will not disappear untill you click close button
if k == 27: # esc key code = 27 # if user press esc key
    cv2.destroyAllWindows()  # Its close all windows
elif k == ord('s'): # if user press 's' key
    cv2.imwrite('lena_copy.png', img) # it will create a copy of this img. First parameter is just name of img
    cv2.destroyAllWindows()
#cv2.destroyWindow() # It close a specific window. We will see in future


