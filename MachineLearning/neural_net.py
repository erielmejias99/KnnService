import numpy as np
import tensorflow as tf
from tensorflow import keras

def neural(x, y):
    x_train = []
    y_train = []
    for i in range(len(x)):
        x_train.append(x[i][:-1])
        y_train.append(x[i][-1])
    x_train = np.array(x_train)
    y_train = np.array(y_train)
    shape_x = x_train.shape

    inputs = keras.Input(shape=(2, ))
    hidden = keras.layers.Dense(8, activation = 'relu')(inputs)
    hidden = keras.layers.Dense(4, activation = 'relu')(hidden)
    predictions = keras.layers.Dense(2, activation = 'relu')(hidden)
    model = keras.models.Model(inputs = inputs, outputs=predictions)

    model.compile(optimizer=keras.optimizers.RMSprop(lr=0.001), loss='mse', metrics=['mae'])

    model.fit(x_train, y_train, epochs=8)

    predicts = model.predict(y)
    return predicts
