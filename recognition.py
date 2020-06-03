import numpy as np
import tensorflow as tf
import cv2

model = tf.keras.models.load_model('model.h5')
image_url = input("Enter your image url:")
image = cv2.imread(image_url)
image = cv2.resize(image, (30, 30))
image = image / 255
image.resize(1, 30, 30, 3)
print(model.predict(image).argmax())