import os
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

app = Flask(__name__)

# Load the pre-trained Keras model (ensure the model path is correct)
model = load_model('model.h5')

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

        print("=========================")

        print(filepath)

        file.save(filepath)
        img = image.load_img(filepath, target_size=(64, 64))  # Adjust target size to your model's expected input
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)  # Model expects images in batches

        predictions = model.predict(img_array)
        result = np.argmax(predictions, axis=1)  # Assuming your model outputs class probabilities

        return jsonify({'prediction': int(result)})
    else:
        return jsonify({'error': 'Allowed file types are ...'}), 400

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}

if __name__ == '__main__':
    app.run(debug=True, port=5000)
