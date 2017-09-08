from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten, Convolution2D, MaxPooling2D
from keras.utils import np_utils
import keras.callbacks
from matplotlib import pyplot as plt
from keras.utils.vis_utils import plot_model as plot
from numpy import *

random.seed(123)
import os.path


def load_data(path, zonepy):
    xtr = fromfile(path + zonepy + "-xtr.bin", dtype=int32)
    ytr = fromfile(path + zonepy + "-ytr.bin", dtype=int32)
    xte = fromfile(path + zonepy + "-xte.bin", dtype=int32)
    yte = fromfile(path + zonepy + "-yte.bin", dtype=int32)
    ytr = np_utils.to_categorical(ytr, 2)
    yte = np_utils.to_categorical(yte, 2)
    xtr.shape = (len(xtr) // 400, 2, 200)
    xte.shape = (len(xte) // 400, 2, 200)
    print("数据加载完毕")
    return xtr, ytr, xte, yte


def train(xtr, ytr, xte, yte):
    model = Sequential()
    model.add(Flatten(input_shape=(2, 200)))
    model.add(Dense(2048, activation='tanh'))
    model.add(Dropout(0.5))
    model.add(Dense(1024, activation='tanh'))
    model.add(Dense(128, activation='tanh'))
    model.add(Dropout(0.2))
    model.add(Dense(2, activation='softmax'))

    model.compile(loss='categorical_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])
    # plot(model, to_file='model.png')

    log_filepath = './tmp/logs'
    tb_cb = keras.callbacks.TensorBoard(log_dir=log_filepath, write_images=1, histogram_freq=1)
    cbks = [tb_cb]
    history = model.fit(xtr, ytr, batch_size=256, nb_epoch=10000, verbose=1, callbacks=cbks, validation_data=(xte, yte))
    # score = model.evaluate(xte, yte, verbose=0)
    # print(score)


if __name__ == '__main__':
    xtr, ytr, xte, yte = load_data('F:/MachineLearning/LOL_train/', 'dx7')
    train(xtr, ytr, xte, yte)
