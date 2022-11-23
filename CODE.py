# Import Import Libraries
import cv2             #For computer vision
import numpy as np     # provides a high-performance multidimensional array



# Creating Haarcascade Variable

nplateCascade = cv2.CascadeClassifier("C://Users//Anurag//Desktop//qc//haarcascade_russian_plate_number.xml")

minarea = 500
count = 0
framewidth = 6400
frameheight = 480



# Number Plate Capturing

web_cap = cv2.VideoCapture(0)
web_cap.set(3,framewidth)
web_cap.set(4,frameheight)
web_cap.set(10,1000) # Brightness id = 10 and 100 intensity level

while True :
    success, img = web_cap.read()

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    numberplates = nplateCascade.detectMultiScale(imgGray, 1.1, 4) # 4 : minimum neighbour


 # Create bounding box

    for (x, y, w, h) in numberplates:
        area = w*h
        if area > minarea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0),2) # (x,y) : Initial points & (x+w,y+h) : Diagonal points
            cv2.putText(img,"Number plate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
            imgRoi = img[y:y+h,x:x+w] # Region of number plate
            cv2.imshow("ROI IMAGE", imgRoi)




# Saving Snap-Shot

    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord("s"):
        cv2.imwrite("C://Users//Anurag//Desktop//qc//Image"+str(count)+".jpg",imgRoi)
        cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(img,"scan saved",(150,265),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
        cv2.imshow("Result",img)
        cv2.waitKey(5000)
        count += 1
