from Preproc import *
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

data = getList()

datagen = ImageDataGenerator(
        rotation_range=15,
        width_shift_range=0.1,
        height_shift_range=0.3,
        shear_range=0.05,
        zoom_range=0.1,
        horizontal_flip=False,
        fill_mode='nearest')

"""
model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=(1, 128, 128)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='keras.losses.categorical_crossentropy',
              optimizer='keras.optimizers.Adadelta()',
              metrics=['accuracy'])
"""

train_generator = datagen.flow(data[0], data[2], batch_size=2, save_to_dir="/home/fabian/projects/fahrstuhl_datenkrake/Camera/preview")

for i in train_generator:
    print(i)
    break
