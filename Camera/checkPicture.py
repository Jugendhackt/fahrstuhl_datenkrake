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

if __name__=="__main__":
    os.chdir(path)
    ml = loadModel(LevelModel(), "levels.hd5")
    ma = loadModel(ArrowModel(), "arrows.hd5")
    for i in glob.glob("Pictures/Pfeile/*.jpg"):
        print(i)
        print(checkPic(ma, sm.imread(i, "L")))
    for i in glob.glob("Pictures/Levels/*.jpg"):
        print(i)
        print(checkPic(ml, sm.imread(i, "L")))

