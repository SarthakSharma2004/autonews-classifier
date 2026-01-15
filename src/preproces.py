import re
from tensorflow.keras.preprocessing.sequence import pad_sequences
from loader import ArtifactsLoader


loader = ArtifactsLoader()

class Preprocessor:
    def __init__(self):
        self.tokenizer = loader.load_tokenizer()
        self.max_len = 200



    def preprocess_text(self, text: str):

        text = text.lower()
        text = re.sub(r'[^a-z0-9\s]', '', text)
        text = ' '.join(text.split())

        seq = self.tokenizer.texts_to_sequences([text])
        pad = pad_sequences(seq, maxlen=self.max_len, padding='post', truncating='post')

        return pad


