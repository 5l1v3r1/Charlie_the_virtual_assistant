import cv2
import numpy as np
import sqlite3
import time

faceDetect= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)
recognizer=cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainningData.yml")
id=0
fontFace = cv2.FONT_HERSHEY_COMPLEX
fontScale = 1
fontColor = (255, 255, 255)
path = 'dataSet'
profile=[]

def getProfile(id):
    global profile
    conn=sqlite3.connect("FaceBase.db")
    cmd="SELECT * FROM People WHERE Id="+str(id)
    cursor=conn.execute(cmd)
    profile=None
    for row in cursor:
        profile=row
    conn.close()
    return profile



def recogniseFace():
    global cam
    global profile
    for i in range (200):
        ret, img = cam.read()
        img=cv2.flip(img,1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceDetect.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            id,conf=recognizer.predict(gray[y:y+h,x:x+w])
            profile=getProfile(id)
            if(profile!=None):
                cv2.putText(img, profile[1], (x,y+h), fontFace, fontScale, fontColor)
        if len(profile)>1:
            name=profile[1]
            print(name)
            return name
recogniseFace()
        
