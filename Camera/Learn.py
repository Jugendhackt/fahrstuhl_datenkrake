from Preproc import *
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import keras

data = getList()

batch_size = 32

datagen = ImageDataGenerator(
        rotation_range=1,
        width_shift_range=0.1,
        height_shift_range=0.3,
        zoom_range=0.1,
        horizontal_flip=False,
        fill_mode='nearest')

model = Sequential()
model.add(Conv2D(8, (5, 5), input_shape=(96, 96, 1)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(4, (5, 5)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
model.add(Dense(8))
model.add(Activation('relu'))
model.add(Dense(17, activation='softmax'))

model.compile(loss=keras.losses.sparse_categorical_crossentropy,
        optimizer=keras.optimizers.Adagrad(lr=0.01),
              metrics=['accuracy'])

train_generator = datagen.flow(data[0], data[2], batch_size=32)
test_generator = datagen.flow(data[1], data[3], batch_size=32)

model.fit_generator(
       train_generator,
       steps_per_epoch=2000 // batch_size,
       epochs=50,
       validation_data=test_generator,
       verbose=2,
       validation_steps=800 // batch_size)
