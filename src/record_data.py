import os
import glob

import numpy as np
import pandas as pd

import cv2 as cv
from time import time_ns

def main(letter: str, num_images: int):
    imgs = []
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame. Exiting ...")
            break
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        gray = cv.flip(gray, 1)
        x1, x2 = 150, 550 # change these values to fit your webcam 
        y1, y2 =  50, 450 # change these values to fit your webcam
        gray = cv.rectangle(gray, (x1, y1), (x2, y2), (0, 1, 0), 4)
        hand = gray[y1:y2, x1:x2]
        hand = cv.resize(hand, (56, 56))
        cv.imshow("frame", gray)
        cv.imshow("hand", cv.resize(hand, (400, 400)))

        imgs.append(hand)

        if len(imgs) == num_images or cv.waitKey(1) == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()

    letter = letter
    save_loc = os.path.join("./live2", letter)
    os.makedirs(save_loc, exist_ok=True)
    for img in imgs:
        id = time_ns()//100000
        try:
            cv.imwrite(os.path.join(save_loc, f"{id}.png"), img)
        except:
            print('imwrite failed')
            pass
    print(f"{len(glob.glob(os.path.join(save_loc, '*.png')))} pictures with the letter: {letter}")

if __name__ == "__main__":
    try:
        main('z_blank', 600)
    except:
        print('failed')
    