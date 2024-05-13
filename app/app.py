import os
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
from keras.preprocessing.image import load_img
import numpy as np

app = Flask(__name__)

# Load the pre-trained Keras model (ensure the model path is correct)
model = load_model('model.h5')

img_width, img_height = 224, 224

@app.route('/hello', methods=['GET'])
def hello_world():
    return "Hello world"

@app.route('/predict', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected for uploading'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join('/tmp', filename)

        file.save(filepath)
        image = load_img(filepath, target_size=(img_width, img_height))  # Adjust target size to your model's expected input
        img = np.array(image)
        img = img / 255.0
        img = img.reshape(1,img_width, img_height,3)
        label = model.predict(img)

        print("Predicted Class (0 - weapons , 1- noweapons): ", label[0][0])

        return jsonify({'prediction': float(label[0][0])})
    else:
        return jsonify({'error': 'Allowed file types are ...'}), 400

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}

if __name__ == '__main__':
    app.run(debug=True, port=5000)
