
# coding: utf-8

# In[1]:


import cv2


# In[2]:


[i for i in dir(cv2) if 'casca' in i] # ['haarcascades']
[i for i in dir(cv2) if 'Casca' in i] # ClasscadeClassifier


# In[3]:


cascl = cv2.CascadeClassifier('face.xml')
dir(cascl)


# In[10]:


cap=cv2.VideoCapture(0)
if cap.isOpened():
  print("Ready")
else:
  print("False")
# calling classifier
cascl=cv2.CascadeClassifier('face.xml')
# loading face data
cap=cv2.VideoCapture(0)

while cap.isOpened():
    status,frame=cap.read()
    
    face=cascl.detectMultiScale(frame,1.13,5)  # classfier tuning parameter [we can change]
    print(face)
    for x,y,h,w in face:
        cv2.rectangle(frame,(x,y),(x+h,y+w),(0,0,255),2)
    cv2.imshow('face',frame)
    if cv2.waitKey(10)&0xff==ord('q'):
        break
cv2.destroyAllWindows()
cap.release()

