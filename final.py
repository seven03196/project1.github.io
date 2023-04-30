import face_recognition
import cv2
import os
import numpy as np

def read_directory(directory_name):
    image0=face_recognition.load_image_file("C:/Users/own/1.jpg")
    face_location = face_recognition.face_locations(image0)
    myEncode=face_recognition.face_encodings(image0)[0]
    names=[]
    scores=[]
    percentage=[]
    for filename in os.listdir(r"C:/Users/"+directory_name):
        for img in os.listdir(r"C:/Users/"+directory_name+"/"+filename):
            image=face_recognition.load_image_file("C:/Users/"+directory_name + "/"+filename+"/"+img)
            try:
                face_location = face_recognition.face_locations(image)
                imagEncode = face_recognition.face_encodings(image)[0]
                names.append(filename)
                distance=face_recognition.face_distance([myEncode],imagEncode)
                value=distance[0]
                scores.append(value)
                eachsimilarity=(1-value)*100
                percentage.append(eachsimilarity)            
            except:
                print()
    min_list=min(scores)
    similarity=(1-min_list)*100
    max_index =scores.index(min_list)
    print("與"+names[max_index]+"明星最像相似度大約="+str(similarity)+"%")
    for filename in os.listdir(r"C:/Users/"+directory_name):
       for img in os.listdir(r"C:/Users/"+directory_name+"/"+filename):
           if(filename==names[max_index]):
               img1="C:/Users/own/1.jpg"    
               img2="C:/Users/"+directory_name+"/"+names[max_index]+"/"+img
               img1=cv2.imdecode(np.fromfile(img1,dtype=np.uint8),-1)
               img2=cv2.imdecode(np.fromfile(img2,dtype=np.uint8),-1)
               resImga=cv2.resize(img1,(250,250),interpolation=cv2.INTER_CUBIC)
               resImgb=cv2.resize(img2,(250,250),interpolation=cv2.INTER_CUBIC)
               cv2.imshow("imga",resImga)
               cv2.imshow("imgb",resImgb)
               cv2.waitKey(0)                         
                              
          
read_directory("明星資料集")