import os
import glob

import numpy as np
import pandas as pd
from PIL import Image

import cv2 as cv
from time import time_ns

def main(num_images: int, save_loc):
    imgs = []
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    for _ in range(10):
        ret, frame = cap.read()
        cv.imshow("frame", frame)
    print(f"Press any key to start recording: {letter}")
    cv.waitKey()
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame. Exiting ...")
            break
        # gray = cv.cvtColor(frame)#, cv.COLOR_BGR2GRAY)
        frame = cv.flip(frame, 1)
        x1, x2 = 250, 450 # change these values to fit your webcam 
        y1, y2 =  150, 350 # change these values to fit your webcam
        frame = cv.rectangle(frame, (x1, y1), (x2, y2), (0, 1, 0), 4)
        hand = frame[y1:y2, x1:x2]
        hand = cv.resize(hand, (56, 56))
        cv.imshow("frame", frame)
        cv.imshow("hand", cv.resize(hand, (400, 400)))

        imgs.append(hand)

        if len(imgs) == num_images or cv.waitKey(1) == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()


    os.makedirs(save_loc, exist_ok=True)
    start_time = time_ns()//100000
    for i, img in enumerate(imgs):
        try:
            cv.imwrite(os.path.join(save_loc, f"{start_time}_{i}.jpg"), img)
        except:
            print('imwrite failed')
            pass

if __name__ == "__main__":
    alphabet = list("abcdefghiklmnopqrstuvwxy") + ['z_blank']
    for letter in alphabet:
        save_loc = os.path.join("./live_color_yuhan", letter)
        num_images = 300

        try:
            main(num_images, save_loc)
            print(f"{len(glob.glob(os.path.join(save_loc, '*.jpg')))} pictures with the letter: {letter}")
        except Exception as e:
            print(f'failed: {e}')
