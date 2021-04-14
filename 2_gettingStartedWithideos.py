import cv2

cap = cv2.VideoCapture(0)  # if you give 0 it will capture from your webcam.
                            # or you can give a video file with full name for example 'myvideo.avi'


fourcc = cv2.VideoWriter_fourcc(*'XVID') # *'XVID' is same as 'X','V','I','D'
                                        # this is specifies the codec. You can look the codecs in link below
                                        # https://www.fourcc.org/codecs.php

out = cv2.VideoWriter('outpu.avi', fourcc, 20.0, (640, 480))  # this is using to save video capture
# the parameters are: output file name, codec, frame per second, size of frame as tuple(width, height)

while cap.isOpened():  # use this func to
    ret, frame = cap.read()  # frame is actual video capture (frame by frame)
                             # ret is returning value of is frame accesible (boolean)

    if ret == True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # it will return width of frame
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # it will return height of frame
        # Other flags in video capturing in the link below
        # https://docs.opencv.org/4.0.0/d4/d15/group__videoio__flags__base.html#gaeb8dd9c89c10a5c63c139bf7c4f5704d

        out.write(frame)  # writes the frame to file

        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # this func converts rgb to gray

        cv2.imshow('frame', frame) # this will show captured video in a window
                                    # if you want to see gray scaled use gray variable instead of frame

        if cv2.waitKey(1) & 0xFF == ord('q'): # if user press key 'q' get out from the loop
            break
    else:
        break
cap.release() # it is important to close video capturing
out.release()
cv2.destroyAllWindows()