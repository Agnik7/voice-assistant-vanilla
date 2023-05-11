import os
import datetime
import cv2 as cv
import speech


def camera():
    cam = cv.VideoCapture(0)
    result, image = cam.read()
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-image.png"
    if result:
        cv.imshow("Picture", image)
        cv.imwrite(file_name, image)
        cv.waitKey(0)
        cv.destroyAllWindows()
        speech.speech("Captured successfully!")
    else:
        speech.speech("No image detected. Please! try again")
