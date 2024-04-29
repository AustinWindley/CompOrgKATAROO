import cv2
import numpy as np

image = cv2.VideoCapture(0)
lower_laser = np.array([0,0,180], dtype="uint8") #lower bound for laser detection
upper_laser = np.array([120,120,255], dtype="uint8") #upper bound

#loop that turns each frame into an image and analyzes it
keep_running = True
while(keep_running):
    
    ret, frame = image.read() #turns the current frame into an image

    cv2.imshow('Frame', frame) #displays base frame
    
    mask = cv2.inRange(frame, lower_laser, upper_laser) #creates a color mask based on laser bounds

    detected_output = cv2.bitwise_and(frame, frame, mask = mask)
    cv2.imshow("Laser Detection", detected_output) #displays isolated colors
    cv2.imshow("mask", mask) #displays specific pixels to look at

    coords = np.transpose(np.nonzero(mask)) #finds any pixels that aren't empty
    
    # checks first coordinate for location and decides which direction to move
    try:  
        if (coords[0][1] > 450):
            print("Turn Left")
        elif (coords[0][1] < 250):
            print("Turn Right")
        else:
            print("Go Forward")
    except:
        print("No Red Pixels: STOP")
    
    # quit loop if "q" is pressed
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        keep_running = False
    
image.release() #stops camera feed

cv2.destroyAllWindows() #closes all windows