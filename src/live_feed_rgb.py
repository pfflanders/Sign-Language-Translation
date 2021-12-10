import cv2 as cv
import numpy as np 
import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense, Softmax
from tensorflow.keras.losses import CategoricalCrossentropy
from tensorflow.keras.metrics import CategoricalAccuracy

def main():
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
    # resnet50_1_color - very good on white background
    # 


    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        ret, frame = cap.read()
        
        if not ret:
            print("Can't receive frame. Exiting ...")
            break
        frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB) # modify this based on what model
        frame = cv.flip(frame, 1)
        x1, x2 =  250, 450 # change these values to fit your webcam 
        y1, y2 =  150, 350 # change these values to fit your webcam
        frame = cv.rectangle(frame, (x1, y1), (x2, y2), (0, 1, 0), 4)
        hand = frame[y1:y2, x1:x2]
        hand = cv.resize(hand, (56, 56))
        font = cv.FONT_HERSHEY_SIMPLEX 
        fontScale = 2
        fontThickness = 3
        color = (255,0,255)
        org = (150,100)

        # convert hand image to array, alter dimensions and values to get guess
        sign = np.asarray(hand)
        sign = sign/255.0
        my_hand = sign[:,:].reshape((1,56,56,3))

        my_guess = model.predict(my_hand)

        accuracy = np.max(my_guess)
        character = np.argmax(my_guess)
        
        
        letter = alphabet[character]
        print(f"Guess: {letter}, Accuracy:{accuracy}")
        print()


        cv.putText(frame,letter,org,font,fontScale,color,fontThickness)
        frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR) # modify this based on what model
        cv.imshow("frame", frame)

        if cv.waitKey(1) == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()

   
if __name__ == "__main__":
        main()
