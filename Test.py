{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "d06d9c18",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Loading Our Model and classifier\n",
    "from keras.models import load_model\n",
    "from time import sleep\n",
    "from keras.preprocessing.image import img_to_array\n",
    "from keras.preprocessing import image\n",
    "import cv2\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "7557706b",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Loading our model and face-detector\n",
    "face_classifier = cv2.CascadeClassifier(r'C:\\Facial Expressions Recognition\\haarcascade_frontalface_default.xml')\n",
    "classifier =load_model(r'C:\\Facial Expressions Recognition\\Emotion_little_vgg.h5')\n",
    "\n",
    "class_labels = ['Angry','Happy','Neutral','Sad','Surprise']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "8a6c8ac6",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Capturing frames from our cam and showing expression as a caption (Press 'q' on keyboard to exit)\n",
    "cap = cv2.VideoCapture(0)\n",
    "\n",
    "\n",
    "while True:\n",
    "    # Grab a single frame of video\n",
    "    ret, frame = cap.read()\n",
    "    labels = []\n",
    "    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)\n",
    "    faces = face_classifier.detectMultiScale(gray,1.3,5)\n",
    "\n",
    "    for (x,y,w,h) in faces:\n",
    "        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)\n",
    "        roi_gray = gray[y:y+h,x:x+w]\n",
    "        roi_gray = cv2.resize(roi_gray,(48,48),interpolation=cv2.INTER_AREA)\n",
    "    # rect,face,image = face_detector(frame)\n",
    "\n",
    "\n",
    "        if np.sum([roi_gray])!=0:\n",
    "            roi = roi_gray.astype('float')/255.0\n",
    "            roi = img_to_array(roi)\n",
    "            roi = np.expand_dims(roi,axis=0)\n",
    "\n",
    "        # make a prediction on the ROI, then lookup the class\n",
    "\n",
    "            preds = classifier.predict(roi)[0]\n",
    "            label=class_labels[preds.argmax()]\n",
    "            label_position = (x,y)\n",
    "            cv2.putText(frame,label,label_position,cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)\n",
    "        else:\n",
    "            cv2.putText(frame,'No Face Found',(20,60),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)\n",
    "    cv2.imshow('Emotion Detector',frame)\n",
    "    if cv2.waitKey(1) & 0xFF == ord('q'):\n",
    "        break\n",
    "\n",
    "cap.release()\n",
    "cv2.destroyAllWindows()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
