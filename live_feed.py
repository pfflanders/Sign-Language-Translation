import cv2 as cv
import numpy as np 
import tensorflow as tf


def main():
    #create alphabet list of potential predictions
    alphabet = list("abcdefghiklmnopqrstuvwxyz")
    #load model
    saved_path = 'testing_models\\full_dense_1'
    
    model = tf.keras.models.load_model(saved_path)
    
    # cap = cv.VideoCapture(0, cv.CAP_DSHOW)
    # Removed CAP_DSHOW
    # if this was necessary then we'll need to figure out why it breaks on my system
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
        font = cv.FONT_HERSHEY_SIMPLEX 
        fontScale = 2
        fontThickness = 3
        color = (0,255,0)
        org = (150,100)

        # convert hand image to array, alter dimensions and values to get guess
        sign = np.asarray(hand)
        sign = sign/255.0
        my_hand = sign[:,:].reshape((1,56,56,1))
        my_hand = (my_hand - my_hand.min())/(my_hand.max() - my_hand.min())

        my_guess = model.predict(my_hand)

        # see overall guesses and probability of guesses
        # guess_vals = {tuple(alphabet):my_guess} 

        accuracy = np.max(my_guess)
        character = np.argmax(my_guess)
        letter = alphabet[character]
        print(f"Guess: {alphabet[character]}, Accuracy:{accuracy}")
        print()
        # print(guess_vals)




        cv.putText(gray,letter,org,font,fontScale,color,fontThickness)
        cv.imshow("frame", gray)
        # I wanted only a single frame for simplicity.
        # cv.imshow("hand", cv.resize(hand, (400, 400)))


        if cv.waitKey(1) == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()

   
if __name__ == "__main__":
        main()
    
    

