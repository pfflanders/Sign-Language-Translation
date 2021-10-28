import numpy as np
import pandas as pd

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import InputLayer, Flatten, Dense, ReLU, Softmax, Conv2D, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.losses import CategoricalCrossentropy
from tensorflow.keras.metrics import CategoricalAccuracy
from tensorflow.keras.optimizers import Adam, RMSprop
from tensorflow.keras.callbacks import TensorBoard, ReduceLROnPlateau, ModelCheckpoint

from low_rank_layer import LowRankDense


def get_data(dataset):
    data = pd.read_csv(f"{dataset}.csv")
    x = np.array(data.drop(columns="label"))
    x = x.reshape((-1, 28, 28, 1))
    x = x.astype(np.float32) / 255
    y = np.array(data["label"])
    y_onehot = np.zeros((len(y), y.max(initial=0) + 1))
    y_onehot[np.arange(len(y)), y] = 1
    return x, y_onehot


def main(training_run: str):
    x_train, y_train = get_data("./dataset/sign_mnist_train")
    x_test, y_test = get_data("./dataset/sign_mnist_test")
    image_generator = ImageDataGenerator(
        rotation_range=20,
        width_shift_range=10,
        height_shift_range=10,
        horizontal_flip=True
    )

    model = Sequential([
    InputLayer(input_shape=(56, 56, 1)),
    Conv2D(64, 5),
    ReLU(),
    Conv2D(64, 3),
    ReLU(),
    Conv2D(64, 3, strides=2),
    ReLU(),
    Dropout(0.2),
    Conv2D(128, 3, strides=2),
    ReLU(),
    Dropout(0.2),
    Conv2D(128, 3, strides=2),
    ReLU(),
    Dropout(0.2),
    Flatten(),
    Dense(512, init_rank=40),
    ReLU(),
    Dense(512, init_rank=20),
    ReLU(),
    Dense(25),
    Softmax(),
])
    model.compile(
        optimizer=Adam(learning_rate=0.001),
        loss=CategoricalCrossentropy(),
        metrics=[CategoricalAccuracy()]
    )
    model.fit(
        image_generator.flow(x_train, y_train, batch_size=64),
        callbacks=[
            ReduceLROnPlateau(monitor="val_loss", factor=0.1, patience=10),
            TensorBoard(log_dir=f"logs_{training_run}"),
            ModelCheckpoint(f"model_{training_run}_ckpt", save_best_only=True)
        ],
        epochs=120,
        validation_data=(x_test, y_test))
    model.save(f"model_{training_run}")


if __name__ == "__main__":
    main("run_5")
