import dill
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

personality_dict = {
    'I': 0,
    'E': 1,
    'N': 0,
    'S': 1,
    'F': 0,
    'T': 1,
    'J': 0,
    'P': 1,
}

types = [
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


def pipeline(X_train, y_train):
    pipeline = Pipeline(
        [
            (
                'counter',
                CountVectorizer(
                    analyzer='word',
                    max_features=1500,
                    tokenizer=None,
                    preprocessor=None,
                    stop_words=stopwords.words('english'),
                    max_df=0.85,
                    min_df=0.05,
                ),
            ),
            (
                'tfidf',
                TfidfTransformer(),
            ),
            (
                'clf',
                LogisticRegression(),
            ),
        ],
    )

    pipeline.fit(X_train, y_train)

    return pipeline


def clean(text):
    lemmatizer = WordNetLemmatizer()

    return ' '.join(
        [lemmatizer.lemmatize(i) for i in text.lower().split() if not len([1 for t in types if t in i])],
    )


def text_preprocess(X):
    X = X.apply(clean)

    preprocessed_word_count = X.apply(
        lambda x: len(x.split()),
    )

    MIN_WORDS = preprocessed_word_count.quantile(0.05)

    return X, preprocessed_word_count >= MIN_WORDS


def main():
    df = pd.read_csv('data/MBTI 500.csv')

    X = df.posts

    y = pd.concat(
        [
            pd.DataFrame.from_records(
                df.type.apply(
                    lambda x: [personality_dict[i] for i in x],
                ).values,
            ),
            df.type,
        ],
        axis=1,
    )

    X, mask = text_preprocess(X)

    X = X[mask]
    y = y[mask]

    X, X_val, y, y_val = train_test_split(X, y, test_size=0.2)

    pipelines = []

    for i in range(4):
        X_train, X_test, y_train, y_test = train_test_split(X, y[i])
        pipelines.append(pipeline(X_train, y_train))

        y_pred = pipelines[-1].predict(X_test)

        print('ROC-AUC: ', roc_auc_score(y_test, y_pred))

        with open(f'data/models/pipeline_{i}.dill', 'wb') as f:
            dill.dump(pipelines[-1], f)


if __name__ == '__main__':
    main()
