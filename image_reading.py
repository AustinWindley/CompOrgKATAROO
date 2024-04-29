import cv2
import numpy as np

image = cv2.VideoCapture(0)
lower_laser = np.array([0,0,180], dtype="uint8")
upper_laser = np.array([100,100,255], dtype="uint8")

keep_running = True
while(keep_running):
    
    ret, frame = image.read()

    cv2.imshow('Frame', frame)
    
    mask = cv2.inRange(frame, lower_laser, upper_laser)

    detected_output = cv2.bitwise_and(frame, frame, mask = mask)
    cv2.imshow("Laser Detection", detected_output)
    cv2.imshow("mask", mask)

    coords = np.transpose(np.nonzero(mask))
    try:  
        if (coords[0][1] > 450):
            print("Turn Left")
        elif (coords[0][1] < 250):
            print("Turn Right")
        else:
            print("Go Forward")
    except:
        print("No Red Pixels: STOP")
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        keep_running = False
    
image.release()

cv2.destroyAllWindows()