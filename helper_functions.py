import pandas as pd 
import os


def convert_image(imag):
    pass

def main():
    dir = r'C:\Users\famil\Pictures\Camera Roll\peter_hands'
    for filename in os.listdir(dir):
        if filename.endswith(".jpg"):
            label = filename[:1]
        