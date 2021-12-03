#Import necessary libraries
from flask import Flask, render_template, Response
import cv2 as cv
import numpy as np 
import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense, Softmax
from tensorflow.keras.losses import CategoricalCrossentropy
from tensorflow.keras.metrics import CategoricalAccuracy

#Initialize the Flask app
app = Flask(__name__)

camera = cv.VideoCapture(0)

#load model weights 
alphabet = list("abcdefghiklmnopqrstuvwxy") + ['blank']
# Compile the Model and Load Weights
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
model.load_weights(r'mobilenet7\variables\variables')

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
            frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

            #create a separate prediction frame so that the quality of the feed does not drop
            #this frame will be reshaped to 56x56 for our model 
            prediction = frame
            prediction = cv.resize(prediction,(56,56),fx=0,fy=0, interpolation = cv.INTER_CUBIC)
            
            #create the box in our frame to help user target the image 
            #potential issue, will the resizing affect the bounds of the image? Is what the user sees in terms of the box what the prediction is actually basing it off of?
            #Ask peter and mansa about this
            x1, x2 = 150, 550 # change these values to fit your webcam 
            y1, y2 =  50, 450 # change these values to fit your webcam
            frame = cv.rectangle(frame,(x1,y1),(x2,y2),(0,1,0),4)
            frame = cv.flip(frame,1)
            
            #predict based on prediction frame above 
            sign = np.asarray(prediction)
            print('sign shape:', sign.shape)
            sign = sign/255.0
            my_hand = sign[:,:].reshape((1,56,56,1))
            print('hand_shape',my_hand.shape)
            my_hand = (my_hand - my_hand.min())/(my_hand.max() - my_hand.min())
            guess = predict(my_hand)
            print('frame shape:',frame.shape)

            ##Format prediction guesses onto frame 
            font = cv.FONT_HERSHEY_SIMPLEX 
            fontScale = 1
            fontThickness = 3
            color = (0,255,0)
            org = (100,90)
            cv.putText(frame,guess,org,font,fontScale,color,fontThickness)
            ret, buffer = cv.imencode('.jpg', frame)
            frame = buffer.tobytes()
            ##output to webpage
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show results
    
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')




if __name__ == "__main__":
    app.run(debug=True)