import keras
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import numpy as np
import scipy.misc as sm
import glob
from TrainArrow import constructModel as ArrowModel
from TrainLevel import constructModel as LevelModel
import os

path = os.path.dirname(os.path.realpath(__file__))


def loadModel(model, weights_path):
    model.load_weights(weights_path)
    return model


def checkPic(model, pic):
    os.chdir(path)

    result = model.predict(np.reshape(pic, (1, 40, 40, 1)), 1, 1)
    return np.argmax(result)


def crop(path):
    """
    Takes latest .jpg out of the given path
    returns arrays showing 1. arrows 2. level
    """
    h = 40
    w = 40
    # offset in y direction
    hoffPfeil = 15
    hoffStock = 10
    os.chdir(path)
    f = glob.glob("*.jpg")[-1]
    im = ndimage.imread(f)
    arrows = im[hoffPfeil:h + hoffPfeil, w + 16:]
    level = im[hoffStock:h + hoffStock, 0:w]
    return arrows, level


if __name__ == "__main__":
    os.chdir(path)
    ml = loadModel(LevelModel(), "levels.hd5")
    ma = loadModel(ArrowModel(), "arrows.hd5")
    for i in glob.glob("Pictures/Pfeile/*.jpg"):
        print(i)
        print(checkPic(ma, sm.imread(i, "L")))
    for i in glob.glob("Pictures/Levels/*.jpg"):
        print(i)
        print(checkPic(ml, sm.imread(i, "L")))
