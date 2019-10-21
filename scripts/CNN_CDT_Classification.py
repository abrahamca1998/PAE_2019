#Set-up
from pathlib import Path
import os
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.callbacks import TensorBoard
from keras.preprocessing.image import ImageDataGenerator
import tensorflow

#Dir ubication

TRAIN_DIR=Path('/home/abraham/Escritorio/PAE_2/pae2019/CLOCK/CDT_images/train')
TEST_DIR=Path('/home/abraham/Escritorio/PAE_2/pae2019/CLOCK/CDT_images/test')
TRAIN_DIR_DEMENTIA=TRAIN_DIR / "dementia"
TRAIN_DIR_HEALTH=TRAIN_DIR / "health"
TEST_DIR_DEMENTIA=TRAIN_DIR / "dementia"
TEST_DIR_HEALTH=TRAIN_DIR / "health"
train_health_images=[(TRAIN_DIR_HEALTH / i).as_posix() for i in os.listdir(TRAIN_DIR_HEALTH)]
train_dementia_images=[(TRAIN_DIR_DEMENTIA /i).as_posix() for i in os.listdir(TRAIN_DIR_DEMENTIA)]
test_health_images=[(TEST_DIR_HEALTH  /i).as_posix() for i in os.listdir(TEST_DIR_HEALTH)]
test_dementia_images=[(TEST_DIR_DEMENTIA /i).as_posix() for i in os.listdir(TEST_DIR_DEMENTIA)]

#CNN model
classifier = Sequential()
classifier.add(Conv2D(32,(3,3),input_shape=(64,64,3),activation = 'relu'))
classifier.add(MaxPooling2D(pool_size=(2,2),strides=2)) #if stride not given it equal to pool filter size
classifier.add(Conv2D(32,(3,3),activation = 'relu'))
classifier.add(MaxPooling2D(pool_size=(2,2),strides=2))
classifier.add(Flatten())
classifier.add(Dense(units=128,activation='relu'))
classifier.add(Dense(units=1,activation='sigmoid'))
adam = tensorflow.keras.optimizers.Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0, amsgrad=False)
classifier.compile(optimizer=adam,loss='binary_crossentropy',metrics=['accuracy'])

train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1./255)


train_set = train_datagen.flow_from_directory(TRAIN_DIR,
                                             target_size=(64,64),
                                             batch_size=32,
                                             class_mode='binary')
test_set = test_datagen.flow_from_directory(TEST_DIR,
                                           target_size=(64,64),
                                           batch_size = 32,
                                           class_mode='binary',
                                           shuffle=False)

classifier.fit_generator(train_set,
                        steps_per_epoch=20, 
                        epochs = 10
                        #callbacks=[tensorboard]
                        )

test_images=test_health_images+test_dementia_images

import numpy as np
from keras.preprocessing import image
predictions=[]
for images in test_images:
    test_image=image.load_img(images,target_size=(64,64))
    test_image=image.img_to_array(test_image)
    test_image=np.expand_dims(test_image,axis=0)
    result=classifier.predict(test_image)
    predictions.append(result[0][0])
 
print(predictions)

            