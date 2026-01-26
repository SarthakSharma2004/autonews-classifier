import pickle 
from tensorflow.keras.models import load_model
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARTIFACTS_PATH = os.path.join(BASE_DIR, "..", "artifacts")


def load_trained_model():
    try:
        return load_model(os.path.join(ARTIFACTS_PATH, "bilstm_tuned_model.keras"))
    
    except Exception as e:
        print("Error loading model: ", e)
        return None


def load_tokenizer():
    try:
        with open(os.path.join(ARTIFACTS_PATH, "tokenizer.pkl"), "rb") as f:
            return pickle.load(f)
    
    except Exception as e:
        print("Error loading tokenizer: ", e)
        return None
    


def load_label_encoder():
    try:
        with open(os.path.join(ARTIFACTS_PATH, "label_encoder.pkl"), "rb") as f:
            return pickle.load(f)
    
    except Exception as e:
        print("Error loading label encoder: ", e)
        return None
    


    
   