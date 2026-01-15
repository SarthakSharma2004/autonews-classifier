from loader import ArtifactsLoader
from preproces import Preprocessor
import numpy as np

loader = ArtifactsLoader()
preprocessor = Preprocessor()


class Classifier:
    """
    This class is responsible for making predictions using the trained model
    """

    def __init__(self):
        self.model = loader.load_trained_model()
        self.preprocessor = preprocessor
        self.le = loader.load_label_encoder()



    def predict(self, text: str):
        """
        This predicts and returns the predicted label
        """

        preprocessed = self.preprocessor.preprocess_text(text)

        probs = self.model.predict(preprocessed)
        
        class_id = probs.argmax(axis = 1)[0]

        label = self.le.inverse_transform([class_id])[0]

        return label


    