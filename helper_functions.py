import os
import glob

import numpy as np
import pandas as pd

import cv2 as cv


def main():
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
        x1, x2 = 150, 550
        y1, y2 =  50, 450
        gray = cv.rectangle(gray, (x1, y1), (x2, y2), (0, 1, 0), 4)
        hand = gray[y1:y2, x1:x2]
        hand = cv.resize(hand, (56, 56))
        cv.imshow("frame", gray)
        cv.imshow("hand", cv.resize(hand, (400, 400)))

        imgs.append(hand)

        if len(imgs) == 1250 or cv.waitKey(1) == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()

    letter = "blank"
    save_loc = os.path.join("./live", letter)
    os.makedirs(save_loc, exist_ok=True)
    for img in imgs:
        id = len(glob.glob(os.path.join(save_loc, "*.png")))
        cv.imwrite(os.path.join(save_loc, f"{id}.png"), img)
    print(f"{len(glob.glob(os.path.join(save_loc, '*.png')))} pictures with the letter: {letter}")

if __name__ == "__main__":
    main()
    