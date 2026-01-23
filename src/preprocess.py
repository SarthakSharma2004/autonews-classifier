from src.loader import load_tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import re


MAX_LEN = 200

def preprocessor(text: str):

    if not text or not isinstance(text, str):
        return None
    
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    text = ' '.join(text.split())

    seq = load_tokenizer().texts_to_sequences([text])
    pad = pad_sequences(seq, maxlen = MAX_LEN, padding='post', truncating='post')

    return pad
