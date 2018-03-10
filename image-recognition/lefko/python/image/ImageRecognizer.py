'''
Created on Jan 31, 2018

@author: lfko
'''
# for plotting things
from matplotlib import pyplot as pl

import numpy as np

# this framework will do the actual image recognition
import cv2


def main():
    # read an image
    # we need to provide a file (or a path to a file) and the color components, we would like to read
    image = cv2.imread('/media/lfko/Lagerraum/Pictures/gruppe-lan.jpg', cv2.COLOR_BGR2GRAY)
    
    # resize by halfing each axis
    image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5) 
    
    # show the imported image; first param is the window' name
    # cv2.imshow('Frame', image)
    
    # wait for user interrupt; press any key
    # cv2.waitKey(0)
    # well, self-explanatory
    # cv2.destroyAllWindows()
    faceRecog(image)
#    showWithMPL(image)


def faceRecog(image):
    # templates for facial recognition
    face_cascade = cv2.CascadeClassifier('opencv/data/haarcascades/haarcascade_frontalface_default.xml')

    # templates for eye recognition
    eye_cascade = cv2.CascadeClassifier('opencv/data/haarcascades/haarcascade_eye.xml')
    
    # gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(image, 1.3, 5)

    for (x, y, w, h) in faces:
        # mark faces with a rectangle
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = image[y:y + h, x:x + w]
        roi_color = image[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            # mark eyes with a rectangle
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
    
    # resize it before showing it
    image = cv2.resize(image, (0, 0), fx=0.7, fy=0.7) 
    cv2.imshow('img', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def showWithMPL(image):
    # now do the same with matplotlib
    pl.imshow(image, cmap='gray', interpolation='bicubic')
    pl.xticks([]), pl.yticks([])  # to hide tick values on X and Y axis
    # this will render a stripe into the image
    pl.plot([200, 300, 400], [100, 200, 300], 'c', linewidth=5)
    pl.show()


if __name__ == "__main__":
    main() 
