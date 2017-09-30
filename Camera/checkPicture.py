import keras
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import numpy as np
import scipy.misc as sm
import glob

def loadModel(path):
    model = Sequential()
    model.add(Conv2D(4, (3, 3), input_shape=(40, 40, 1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    
    model.add(Conv2D(4, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    
    model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
    model.add(Dense(16))
    model.add(Activation('relu'))
    model.add(Dense(6, activation='softmax'))
    
    model.compile(loss=keras.losses.sparse_categorical_crossentropy,
            optimizer=keras.optimizers.SGD(lr=0.0001,momentum=0.2),
                  metrics=['accuracy'])

    model.load_weights(path)
    return model

def checkPic(model, pic):
    
    return(model.predict(np.reshape(pic, (1, 40, 40, 1)), 1, 1))

if __name__=="__main__":
    m = loadModel("weights.hd5")
    for i in glob.glob("Pictures/*.jpg"):
        print(checkPic(m, sm.imread(i, "L")))

