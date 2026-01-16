import pickle
from tensorflow.keras.models import load_model
import os


# Path to the artifacts
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARTIFACTS_PATH = os.path.join(BASE_DIR, "..", "artifacts")




class ArtifactsLoader:
    """
    This class is responsible for loading all trained artifacts
    required for inference:
    - Trained BiLSTM model
    - Tokenizer
    - Label Encoder
    """

    def __init__(self):
        self.model_path = os.path.join(ARTIFACTS_PATH, "bilstm_tuned_model.keras")
        self.tokenizer_path = os.path.join(ARTIFACTS_PATH, "tokenizer.pkl")
        self.le_path = os.path.join(ARTIFACTS_PATH, "label_encoder.pkl")

    def load_trained_model(self):
        """This method loads the trained BiLSTM model"""

        try:
            return load_model(self.model_path)
        
        except Exception as e:
            raise RuntimeError(f"Failed to load model: {e}")
        
    

    def load_tokenizer(self):
        """This method loads the tokenizer"""

        try:

            with open(self.tokenizer_path, "rb") as f:
                return pickle.load(f)
            
        except Exception as e:
            raise RuntimeError(f"Failed to load tokenizer: {e}")
        
        
    def load_label_encoder(self):
        """This method loads the label encoder"""

        try:
            with open(self.le_path, "rb") as f:
                return pickle.load(f)
            
        except Exception as e:
            raise RuntimeError(f"Failed to load label encoder: {e}")