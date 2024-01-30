import cv2
import numpy as np

cam = cv2.VideoCapture(0)

classifier  = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml') # face classifier
if cam.isOpened() == False:
    print("somethings wrong i can feel it")
while cam.isOpened:
    ret,frame= cam.read()
    if ret == True:
        face = classifier.detectMultiScale(frame, scaleFactor=1.3, minNeighbors=6)
        
        for x,y,w,h in face:
          cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
          if len(face) > 1:
              cv2.putText(frame , text=str(len(face))+" people", org=(50,50), fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=1,color=(250,0,0),thickness=3)
          else :
              cv2.putText(frame , text=str(len(face))+" person", org=(50,50), fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=1,color=(250,0,0),thickness=3)    
          cv2.putText(frame,text="person",org=(x-10,y-10),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=2,color=(250,0,0),thickness=1)
          
        frame = cv2.resize(frame, (1500,1000), fx=0, fy=0, interpolation=cv2.INTER_AREA)
        cv2.imshow('video dosya okuma', frame)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    else:
        break
cam.release()
cv2.destroyAllWindows()    