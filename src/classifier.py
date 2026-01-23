from src.loader import load_trained_model, load_label_encoder
from src.preprocess import preprocessor
import numpy as np

model = load_trained_model()
label_encoder = load_label_encoder()

def predict_class(text: str):

    preprocessed_text = preprocessor(text)

    if preprocessed_text is None:
        return "Unknown"
    
    try:
        probs = model.predict(preprocessed_text)

        class_id = np.argmax(probs, axis = 1)[0]

        label = label_encoder.inverse_transform([class_id])[0]

        return label

    except Exception:
        return "Unknown"



  