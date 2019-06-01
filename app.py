import os
from flask import Flask , render_template , request , flash , redirect , url_for
import numpy as np
import tensorflow as tf
global hub
import tensorflow_hub as hub
from tensorflow import keras
import tensorflow.keras.backend as K
from tensorflow.keras.preprocessing import image
from model.labels import label_names
import model.formatter as ft
import model.load_model as lm
import static.predictor as pd
import wikipediaapi as wp
import image_downloader as imd
import random_initializer as rni


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

choices = ['' , '' , '']
i , j , z , k , l , m = rni.initializer()
req_label = label_names[i]
req_label = ft.formatString(req_label)
choices[k] = req_label
choices[l] = ft.formatString(label_names[j])
choices[m] = ft.formatString(label_names[z])

wiki = wp.Wikipedia('en')
breed_descr = ''
search = ''
global model , graph
feature_extractor_url = 'https://tfhub.dev/google/imagenet/inception_v3/feature_vector/3'
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
app.config['UPLOAD_FOLDER'] = os.path.join(APP_ROOT , 'static/')
model , graph = lm.ModelInitializer()
prediction_str =""
page = 'index'

@app.route('/')
def index():
    return render_template('materialize_index.html' , page = page)

@app.route('/predict' , methods=['GET' , 'POST'])
def predict():
    target = os.path.join(APP_ROOT , 'static/')
    if not os.path.isdir(target):
        os.mkdir(target)
    filename =""
    for file in request.files.getlist('file'):
        filename = file.filename
        if filename == "":
            flash('Please input an image...')
            return redirect(url_for('index'))
        #filename = "test.jpeg"
        dest = '/'.join([target , filename])
        file.save(dest)

    pred_target = 'static/'+filename
    prediction = pd.Predict(pred_target , model , graph)
    search = prediction.replace(' ' , '_')
    search = prediction.replace('-' , '_')
    search = 'https://en.wikipedia.org/wiki/' + search
    prediction_str = "This is a "+str(prediction)
    breed = wiki.page(str(prediction))
    breed_descr = breed.summary
    #print(breed_descr.summary)
    img_file = 'static/'+filename
    page = 'predict'
    return render_template('materialize_index.html' , pred = prediction_str , img_data = img_file , page = page , summary = breed_descr , search = search)

@app.route('/quiz' , methods=['GET' , 'POST'])
def quiz():
    img_src = imd.find_image(req_label)
    pred_target = 'static/'+img_src
    prediction = pd.Predict(pred_target , model , graph)
    return render_template('quiz.html' , rand_img=str(img_src) , pred=str(prediction) , correct=req_label , choices=choices , page=page)

if __name__ == '__main__':
    app.run(debug=True)