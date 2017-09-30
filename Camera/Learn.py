from Preproc import *
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import keras

data = getList()

batch_size = 64

datagen = ImageDataGenerator(
        rotation_range=1,
        width_shift_range=0.05,
        height_shift_range=0.05,
        zoom_range=0.05,
        horizontal_flip=False,
        fill_mode='nearest')

datagen_small = ImageDataGenerator(
        width_shift_range=0.05,
        height_shift_range=0.05,
        horizontal_flip=False,
        fill_mode='nearest')

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
model.add(Dense(17, activation='softmax'))

model.compile(loss=keras.losses.sparse_categorical_crossentropy,
        optimizer=keras.optimizers.SGD(lr=0.0001,momentum=0.2),
              metrics=['accuracy'])

train_generator = datagen.flow(data[0], data[2], batch_size=64)
test_generator = datagen_small.flow(data[1], data[3], batch_size=64)

model.fit_generator(
       train_generator,
       steps_per_epoch=2000 // batch_size,
       epochs=150,
       validation_data=test_generator,
       verbose=2,
       validation_steps=800 // batch_size)
