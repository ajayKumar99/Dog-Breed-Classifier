import tensorflow as tf
import tensorflow_hub as hub
from tensorflow import keras
import tensorflow.keras.backend as K

def ModelInitializer():
    #Inception model's bottom layer as feature extractor.
    feature_extractor_url = 'https://tfhub.dev/google/imagenet/inception_v3/feature_vector/3'
    #Loading the trained dog classification model
    model = tf.contrib.saved_model.load_keras_model('saved_model')
    model.summary()
    #Variables Intialization
    sess = K.get_session()
    init = tf.global_variables_initializer()
    sess.run(init)
    #Loading trained weights
    model.load_weights('saved_model/model.h5')
    #Compiling the model    
    model.compile(
        optimizer=tf.train.AdamOptimizer(),
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )

    graph = tf.get_default_graph()
    return model , graph
