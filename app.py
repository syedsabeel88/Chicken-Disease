from flask import Flask, render_template,request, jsonify
import os
from flask_cors import CORS, cross_origin #These are used for handling 
# Cross-Origin Resource Sharing (CORS) to allow web applications to make requests to a different domain.
from cnnClassifier.utils.common import decode_image
from cnnClassifier.pipeline.Predict import PredictionPipeline

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)


@app.route('/', methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route('/train', methods=['GET', 'POST'])
@cross_origin()
def trainroute():
    os.system("python main.py")
    return "Training done successfully"


@app.route('/predict', methods=['POST'])
@cross_origin()
def predictroute():
    image = request.json['image']
    decode_image(image, clApp.filename)
    result = clApp.classifier.predict()
    return jsonify(result)


if __name__ == '__main__':
    clApp = ClientApp()
    app.run(host='0.0.0.0', port=8080)