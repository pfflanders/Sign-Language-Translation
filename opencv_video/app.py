# Importing relevant packages
from flask import Flask, g, render_template, request
from PIL import Image

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
            model.load_weights(r'../models/mobilenet7/variables/variables')

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