import cv2 as cv,mediapipe as mp,numpy as np,os


selfieSegmentation = mp.solutions.selfie_segmentation


images=[]                                



directory_path=input("Enter the path of the database\n")
dir_path=os.listdir(directory_path)



for path in os.listdir(directory_path):
        track=os.path.join(directory_path,path)
        img = cv.imread(track,cv.IMREAD_COLOR)
        images.append(track)





print(dir_path)
x=int(input("Enter the index of the image from the above list "))
if(x<=len(images)):
  backgroundImage = cv.imread(images[x-1])
else:
  print("index out of range")
  

cap = cv.VideoCapture(0)

with selfieSegmentation.SelfieSegmentation(model_selection=0) as selfieSeg:
  while cap:
    ret, img = cap.read()
    if ret:
      img=cv.cvtColor(cv.flip(cv.cvtColor(img,cv.COLOR_BGR2RGB), 1),cv.COLOR_RGB2BGR)
      decider = np.stack((selfieSeg.process(img).segmentation_mask,) * 3, axis=-1) > 0.2
      processedImg = np.where(decider, img, backgroundImage)
      cv.imshow('Background Remover', processedImg)
      if cv.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv.destroyAllWindows() 


  

    
    

