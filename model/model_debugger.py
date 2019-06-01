import tensorflow as tf
import tensorflow_hub as hub
from tensorflow import keras
from labels import label_names
from formatter import formatString

feature_extractor_url = 'https://tfhub.dev/google/imagenet/inception_v3/feature_vector/3'
model = tf.contrib.saved_model.load_keras_model('.\\saved_model')
model.summary()
import tensorflow.keras.backend as K
sess = K.get_session()
init = tf.global_variables_initializer()
sess.run(init)
model.load_weights('.\\saved_model\\model.h5')
model.compile(
    optimizer=tf.train.AdamOptimizer(),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)
import numpy as np
IMAGE_SIZE = [299 , 299]
from tensorflow.keras.preprocessing import image
image1 = image.load_img('.\\model\\thumbnail-1477089693232.jpg' , target_size=IMAGE_SIZE)
img_tensor = image.img_to_array(image1)
img_tensor = np.expand_dims(img_tensor , axis=0)
img_tensor /= 255.
print(img_tensor.shape)
result_batch = model.predict(img_tensor)

labels_batch = label_names[np.argmax(result_batch, axis=-1)]
unformatted_prediction = labels_batch[0]
prediction = formatString(unformatted_prediction)
print(prediction)
#model.predict()