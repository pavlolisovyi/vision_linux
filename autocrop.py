import cv2
import sys
import glob 

def main():
    cascPath = "haarcascade_frontalface_default.xml"

    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(cascPath)

    files=glob.glob("cropped.jpg")   
    for file in files:

        # Read the image
        image = cv2.imread(file)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Detect faces in the image
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            # flags = cv2.CV_HAAR_SCALE_IMAGE
        )

        print ("Found {0} faces!".format(len(faces)))

        # Crop Padding
        left = 10
        right = 10
        top = 10
        bottom = 10

        #assigning vars if not assigned
        can_be_analyzed = 1
        try:
            y
        except NameError:
            print("y is not defined at all!!!!")
            y = 5
            can_be_analyzed = 0
        else:
            print("y is good")

        try:
            x
        except NameError:
            print("x is not defined at all!!!!")
            x = 5
            can_be_analyzed = 0
        else:
            print("x is good")

        try:
            h
        except NameError:
            print("h is not defined at all!!!!")
            h = 5
            can_be_analyzed = 0
        else:
            print("h is good")

        try:
            w
        except NameError:
            print("w is not defined at all!!!!")
            w = 5
            can_be_analyzed = 0
        else:
            print("w is good")


        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            print (x, y, w, h)

            # Dubugging boxes
            # cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)


        image  = image[y-top:y+h+bottom, x-left:x+w+right]

        print ("cropped_{1}{0}".format(str(file),str(x)))
        cv2.imwrite("cropped.jpg", image)
        return  can_be_analyzed