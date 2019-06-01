import numpy as np
from tensorflow.keras.preprocessing import image



def InputImageGenerator(path):
    IMAGE_SIZE = [299 , 299]
    image1 = image.load_img(path , target_size=IMAGE_SIZE)
    img_tensor = image.img_to_array(image1)
    img_tensor = np.expand_dims(img_tensor , axis=0)
    img_tensor /= 255.

    return img_tensor