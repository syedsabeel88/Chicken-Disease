import numpy as np
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image


class PredictionPipeline:
    def __init__(self,filename):
        self.filename = filename

    def predict(self):
        model = load_model(os.path.join("artifacts","training","model.h5"))

        imagename = self.filename
        test_image = image.load_img(imagename, target_size= (224,224))
        test_image = image.img_to_array(test_image)
        '''extra dimension is added because deep learning models typically 
        expect a batch of images as input, even if you're processing a single image'''
        test_image = np.expand_dims(test_image, axis=0) 
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)

        if result[0] == 1:
            prediction = 'Healthy'
            return [{"image": prediction}]
        else:
            prediction = 'Coccidiosis'
            return [{"image": prediction}]
