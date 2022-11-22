import numpy as np
import cv2 as cv
import matplotlib.image as image
import mediapipe as mp
import matplotlib.pyplot as plt
import math as mt
import time
import os

listFileDataset = []

# FUNCTIONS
def resize(filename):
    resized = cv.resize(filename, (256, 256))
    return resized

def grayscale(filename):
    gray = cv.cvtColor(filename, cv.COLOR_BGR2GRAY)
    return gray

def changebg(filename):
    # Initialize segmentation
    background_mp = mp.solutions.selfie_segmentation
    background_segment = background_mp.SelfieSegmentation()

    # read image file
    img = cv.imread(filename)

    # convert the BGR format image to an RGB format
    RGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    result = background_segment.process(RGB)

    # binary masking to mask person image
    mask = result.segmentation_mask > 0.9

    # convert to 3-channel
    mask_3_channel = np.dstack((mask,mask,mask))

    # change background color to white
    output = np.where(mask_3_channel, img, 255)  

    # write result to an image file
    return output

def changebgPhoto(filename):
    # Initialize segmentation
    background_mp = mp.solutions.selfie_segmentation
    background_segment = background_mp.SelfieSegmentation()

    # read image file
    img = (filename)

    # convert the BGR format image to an RGB format
    RGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    result = background_segment.process(RGB)

    # binary masking to mask person image
    mask = result.segmentation_mask > 0.9

    # convert to 3-channel
    mask_3_channel = np.dstack((mask,mask,mask))

    # change background color to white
    output = np.where(mask_3_channel, img, 255)  

    # write result to an image file
    return output

def cropface(file):

    # Convert into grayscale
    gray = cv.cvtColor(file, cv.COLOR_BGR2GRAY)
    
    # Load the cascade
    cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_alt2.xml')
    
    # Detect faces
    faces = cascade.detectMultiScale(gray, 1.1, 4)
    
    if len(faces) != 1:
        return None

    # Draw rectangle around the faces and crop the faces
    for (x, y, w, h) in faces:
        cv.rectangle(file, (x, y), (x+w, y+h), (0, 0, 255), 2)
        faces = file[y:y + h, x:x + w]
        return faces

# Function preprocess image
def preprocess(dir):
    global listFileDataset
    S = np.empty((0, 256*256), int)
    for root, dirs, files in os.walk(dir):
        for filename in files:
            # print(os.path.join(root, filename))
            addr = os.path.join(root, filename)
            # change background to white
            pic = changebg(addr)
            # detect and crop face
            face = cropface(pic)

            if face is None:
                continue
                
            # Resize image to 256 x 256
            resized = resize(face)
            # convert to grayscale
            gray_image = grayscale(resized)

            # append to array of image matrixs
            S = np.append(S, [gray_image.flatten()], axis=0)
            
            listFileDataset.append(os.path.join(root,filename))
    return S

def preprocessFile(dir):
    S = np.empty((0, 256*256), int)

    # change background to white
    pic = changebg(dir) # kalau pic belum bisa 
    # detect and crop face
    face = cropface(pic)
        
    print(face.shape)
    # Resize image to 256 x 256
    resized = resize(face)
    # convert to grayscale
    gray_image = grayscale(resized)

    # append to array of image matrixs
    S = np.append(S, [gray_image.flatten()])
    return S

def preprocessPhoto(dir):
    S = np.empty((0, 256*256), int)

    # change background to white
    pic = changebgPhoto(dir) # kalau pic belum bisa 
    # detect and crop face
    face = cropface(pic)
    print(face.shape)
    print('sudah sesuai')
    # Resize image to 256 x 256
    
    resized = resize(face)
    # convert to grayscale
    gray_image = grayscale(resized)

    # append to array of image matrixs
    S = np.append(S, [gray_image.flatten()])
    return S

