from flask import Flask, g, render_template, request
from PIL import Image

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
            # Retrieve the image of hand gesture
            # img = cv2.imread("image",mode='RGB')
            img = Image.open("image")
            img = np.asarray(img)

            # reshape into appropriate format for prediction
            # Image resolution = (56 x 56)
            x = img.reshape(1, 3136)

            # load pre-trained model and get prediction
            # Reference to model included here
            sign = "A"

            # plot the image itself
            fig = Figure(figsize = (3, 3))
            ax = fig.add_subplot(1, 1, 1,)
            ax.imshow(img, cmap = "binary")
            ax.axis("off")

            # Plotting on Flask
            pngImage = io.BytesIO()
            FigureCanvas(fig).print_png(pngImage)

            # Encode PNG image to base64 string
            pngImageB64String = "data:image/png;base64,"
            pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')

            # Render the template with the prediction and image
            return render_template('submit.html', letter=sign, image=pngImageB64String)
        except:
            return render_template('submit.html', error=True)