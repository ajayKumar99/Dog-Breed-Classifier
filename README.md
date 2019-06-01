# Dog Breed Classifier
* A Dog Breed Classification model trained using transfer learning on a pre-trained inception model.
* The bottom layer of inception model is being used as a feature extracting layer and the top layer is swapped with custom dog breed layer.

### Dependencies
Tensorflow has been used to train the model. Further , a Flask app has been made to deploy the model into a web app.
* Tensorflow
* Tensorflow Hub
* Flask
* Wikipedia API

All the dependencies are in the requirements.txt file with the versions used.
A virtual environment is recommended, the following command can be used to build a virtual environment in the project root folder.
```
python -m venv env
```

Then , all the dependencies can be installed from the requirements.txt file using the following command.
```
pip install -r requirements.txt
```
## Dataset
The [Stanford Dogs Dataset](http://vision.stanford.edu/aditya86/ImageNetDogs/images.tar) is used , which contains images of 120 breeds of dogs from around the world and has over 20000 dog images.

## Training the model
The model was built using tensorflow on Google Colab which provides free K80 GPU support for training the model. The custom top layer is added as a Keras Sequential layer with softmax activation.
The model is compiled using Adam Optimizer and loss function as Categorical-Crossentropy.
All the training details and code can be found in this jupyter notebook :- [Dog Breed Training](https://github.com/ajayKumar99/Dog-Breed-Classifier/blob/master/training/dog_breed_classification.ipynb) 
## APIs Used
* [Wikipedia API](https://pypi.org/project/Wikipedia-API/) - For finding details of all the predicted dog, as part of web app feature.
* [Material Design Lite](https://getmdl.io/started/index.html#download) - A light weight material design ui for static html pages. 

## Setting up the app
* Install all the dependencies as mentioned above.
### Running the app in debug mode
* The flask server has to be restarted everytime a change is made to see the changes. So, the server can be used in debug mode which enables auto-restarting of server whenever a change is reflected on any file.
Change the app.run() as follows:
```
app.run(debug=True)
```
### Starting the server
* The flask server can be started by the following command:
```
python app.py
```
All the details of the host address(http://127.0.0.1:5000) will be given just go to the address and the app can be used.
