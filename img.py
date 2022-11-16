import numpy as np
import cv2
import matplotlib.image as image
import mediapipe as mp
import matplotlib.pyplot as plt
import os

# FUNCTIONS
def resize(filename):
    resized = cv2.resize(filename, (256, 256))
    return resized

def grayscale(filename):
    gray = cv2.cvtColor(filename, cv2.COLOR_BGR2GRAY)
    return gray

def changebg(filename):
    # Initialize segmentation
    change_background_mp = mp.solutions.selfie_segmentation
    change_bg_segment = change_background_mp.SelfieSegmentation()

    # read image file
    sample_img = cv2.imread(filename)

    # convert the BGR format image to an RGB format
    RGB_sample_img = cv2.cvtColor(sample_img, cv2.COLOR_BGR2RGB)

    result = change_bg_segment.process(RGB_sample_img)

    # binary masking to mask person image
    binary_mask = result.segmentation_mask > 0.9

    # convert to 3-channel
    binary_mask_3 = np.dstack((binary_mask,binary_mask,binary_mask))

    # change background color to white
    output_image = np.where(binary_mask_3, sample_img, 255)  
    # ss = np.asmatrix(output_image)  

    # write result to an image file
    return output_image

def cropface(file):
    # Read the input image
    # img = cv2.imread(filename)
    
    # Convert into grayscale
    gray = cv2.cvtColor(file, cv2.COLOR_BGR2GRAY)
    
    # Load the cascade
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml')
    
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    # Draw rectangle around the faces and crop the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(file, (x, y), (x+w, y+h), (0, 0, 255), 2)
        faces = file[y:y + h, x:x + w]
        cv2.imshow("face",faces)
        cv2.imwrite('face.jpg', faces)
        
    # Display the output
    cv2.imwrite('detcted.jpg', file)
    cv2.imshow('img', file)
    cv2.waitKey()
    return faces

# Function preprocess image
def preprocess(dir,address,name):
    S = []
    # S = [0 for x in range(10)]
    for root, dirs, files in os.walk(dir):
        i = 0
        for filename in files:
            print(os.path.join(root, filename))
            addr = os.path.join(root, filename)
            # change background to white
            pic = changebg(addr)
            # detect and crop face
            face = cropface(pic)
            # Resize image to 256 x 256
            resized = resize(face)
            # convert to grayscale
            gray_image = grayscale(resized)
            cv2.imwrite(name + str(i) + '.jpg', gray_image)
            img = image.imread(name + str(i) + '.jpg')
            # append to array of image matrixs
            print(img)
            S.append(img)
            # S[i] = img
            # print(S)
            i += 1
    # print(S)
    print(S[1])
    return S


# define address and filename
address = 'C:\\Users\\naufa\\OneDrive\\Documents\\C FIles\\Tubes Algeo 2'
dir = 'dataset'
name = "fly"
file = 'sample.jpeg'

# call function
preprocess(dir,address,name)

# convert to matrix
# img = image.imread('C:/Users/naufa/OneDrive/Documents/C FIles/Tubes Algeo 2/fly0.jpg')
# print('The Shape of the image is:',img.shape)
# print(img)