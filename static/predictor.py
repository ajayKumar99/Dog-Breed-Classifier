import numpy as np
import tensorflow as tf
from tensorflow import keras
import tensorflow.keras.backend as K
from tensorflow.keras.preprocessing import image
from model.labels import label_names
import model.formatter as ft
import model.imagegenerator as im


def Predict(path , model , graph1):
    img_tensor = im.InputImageGenerator(path)
    with tf.Session(graph=graph1) as sess:
        init = tf.global_variables_initializer()
        sess.run(init)
        model.load_weights('saved_model/model.h5')
        result = model.predict(img_tensor)
        labels = label_names[np.argmax(result, axis=-1)]
        unformatted_prediction = labels[0]
        prediction = ft.formatString(unformatted_prediction)
        return prediction

