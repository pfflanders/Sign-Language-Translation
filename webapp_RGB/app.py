# Importing relevant packages
from flask import Flask, g, render_template, request, Response
from PIL import Image
import cv2 as cv
import tensorflow as tf
from tensorflow import keras

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import InputLayer, Flatten, Dense, ReLU, Softmax, Conv2D, Dropout, BatchNormalization
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import CategoricalCrossentropy
from tensorflow.keras.metrics import CategoricalAccuracy

import sklearn as sk
import matplotlib.pyplot as plt
import numpy as np
import pickle

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

import io
import base64

app = Flask(__name__)

camera = cv.VideoCapture(0)

#create alphabet list of potential predictions
alphabet = list("abcdefghiklmnopqrstuvwxy") + ['blank']

IMG_SIZE = (56,56)
IMG_SHAPE = IMG_SIZE + (3,)
base_model = tf.keras.applications.ResNet50V2(input_shape=IMG_SHAPE, include_top=False, weights=None, pooling="avg")

model = Sequential([
base_model,
    Flatten(),
    Dense(25),
    Softmax(),
])
model.compile(
    optimizer="adam",
    loss=CategoricalCrossentropy(),
    metrics=[CategoricalAccuracy()]
)
model.load_weights(r'..\models\resnet50_1_color\variables\variables')


def predict(image):
    '''takes in a frame from video and makes prediction on guess'''

    my_guess = model.predict(image)

    accuracy = np.max(my_guess)
    character = np.argmax(my_guess)
    letter = alphabet[character]
    print(f"Guess: {alphabet[character]}, Accuracy:{accuracy}")
    print()
    return (f"Guess: {alphabet[character]}")


       

def gen_frames():
    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            #predict(frame)
            #keep the frame but make the prediction
            frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

            #create a separate prediction frame so that the quality of the feed does not drop
            #this frame will be reshaped to 56x56 for our model 
            x1, x2 = 250, 450 # change these values to fit your webcam 
            y1, y2 =  150, 350 # change these values to fit your webcam
            prediction = frame[y1:y2,x1:x2]
            prediction = cv.resize(prediction,(56,56),fx=0,fy=0, interpolation = cv.INTER_CUBIC)
            
            #create the box in our frame to help user target the image 
            #potential issue, will the resizing affect the bounds of the image? Is what the user sees in terms of the box what the prediction is actually basing it off of?
            #Ask peter and mansa about this
            frame = cv.rectangle(frame,(x1,y1),(x2,y2),(0,1,0),4)
            frame = cv.flip(frame,1)
            
            #predict based on prediction frame above 
            sign = np.asarray(prediction)
            #print('sign shape:', sign.shape)
            sign = sign/255.0
            my_hand = sign[:,:].reshape((1,56,56,3))
            #print('hand_shape',my_hand.shape)
            my_hand = (my_hand - my_hand.min())/(my_hand.max() - my_hand.min())
            guess = predict(my_hand)
            #print('frame shape:',frame.shape)

            ##Format prediction guesses onto frame 
            font = cv.FONT_HERSHEY_SIMPLEX 
            fontScale = 1
            fontThickness = 3
            color = (255,0,255)
            org = (150,100)
            frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR) # modify this based on what model
            cv.putText(frame,guess,org,font,fontScale,color,fontThickness)
            ret, buffer = cv.imencode('.jpg', frame)
            frame = buffer.tobytes()
           
            ##output to webpage
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show results

@app.route("/")
def main():
    return render_template("main.html")

@app.route("/submit/", methods=["POST", "GET"])
def submit():
    if request.method == "GET":
        return render_template("submit.html")
    else:
        try:
            alphabet = list("abcdefghiklmnopqrstuvwxy") + ['blank']

            # Retrieve the image of hand gesture
            img = Image.open(request.files['image'].stream)
            img = np.asarray(img)

            # Alter the shape of array to get asl_guess
            img = img/255.0
            x = img[:,:].reshape((1,56,56,1))
            x = (x - x.min())/(x.max() - x.min())

            # load pre-trained model and get prediction
            IMG_SIZE = (56,56)
            IMG_SHAPE = IMG_SIZE + (1,)
            base_model = tf.keras.applications.MobileNetV2(input_shape=IMG_SHAPE, include_top=False, weights=None)

            model = Sequential([
                base_model,
                Flatten(),
                Dense(25),
                Softmax(),
            ])
            model.compile(
                optimizer="adam",
                loss=CategoricalCrossentropy(),
                metrics=[CategoricalAccuracy()]
            )
            model.load_weights(r'../models/mobilenet8/variables/variables')

            asl_guess = model.predict(x)
            accuracy = np.round(np.max(asl_guess)*100, 2)
            character = np.argmax(asl_guess)
            sign = alphabet[character]

            # plot the image itself
            fig = Figure(figsize = (4, 4))
            ax = fig.add_subplot(1, 1, 1,)
            ax.imshow(img, cmap = "gray")
            ax.axis("off")

            # Plotting on Flask
            pngImage = io.BytesIO()
            FigureCanvas(fig).print_png(pngImage)

            # # Encode PNG image to base64 string
            pngImageB64String = "data:image/png;base64,"
            pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')

            # Render the template with the prediction and image
            return render_template('submit.html', letter=sign, acc=accuracy, image=pngImageB64String)
        except:
            return render_template('submit.html', error=True)
@app.route('/video')
def index():
        return render_template('index.html')


@app.route('/video_feed')
def video_feed():
        return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
