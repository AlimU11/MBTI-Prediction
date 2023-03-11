import re

import dill
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


class Model:
    def __init__(self):

        self.MIN_WORDS = 520  # TODO: change

        self.personality_dict = {
            '00': 'i',
            '01': 'e',
            '10': 'n',
            '11': 's',
            '20': 'f',
            '21': 't',
            '30': 'j',
            '31': 'p',
        }

        self.types = [
            'infj',
            'entp',
            'intp',
            'intj',
            'entj',
            'enfj',
            'infp',
            'enfp',
            'isfp',
            'istp',
            'isfj',
            'istj',
            'estp',
            'esfp',
            'estj',
            'esfj',
        ]

        self.pipelines = []

        for i in range(4):
            with open(f'data/models/pipeline_{i}.dill', 'rb') as f:
                self.pipelines.append(dill.load(f))

        self.tokens = []

    def predict(self, text):
        text = self.text_preprocess(text)

        self.tokens = text.split()

        pred_type = {}

        for i, pipeline in enumerate(self.pipelines):
            pred = pipeline.predict_proba([text])
            pred_type[self.personality_dict[f'{i}{pred.argmax()}']] = pred.max()

        return ''.join(list(pred_type.keys())), list(pred_type.values())

    def clean(self, text):
        lemmatizer = WordNetLemmatizer()
        stopwords_ = stopwords.words('english')

        return ' '.join(
            [
                lemmatizer.lemmatize(i)
                for i in text.lower().split()
                if i not in stopwords_ and not len([1 for t in self.types if t in i])
            ][: self.MIN_WORDS],
        )

    def text_preprocess(self, text):
        text = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', ' ', text)
        text = re.sub(r'[^a-zA-Z]', ' ', text)
        return self.clean(text)
