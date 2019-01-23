'''
    Created on Jan 14, 2019

    @author: fb
'''
import os, gzip
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
import urllib.request

import numpy as np
import pandas as pd

DATADIR = "data"


def load_data():
    if not os.path.exists(DATADIR): 
        os.mkdir(DATADIR)

    file_name = os.path.join(DATADIR, 'bundestags_parlamentsprotokolle.csv.gzip')
    if not os.path.exists(file_name):
        url_data = 'https://www.dropbox.com/s/1nlbfehnrwwa2zj/bundestags_parlamentsprotokolle.csv.gzip?dl=1'
        urllib.request.urlretrieve(url_data, file_name)

    df = pd.read_csv(gzip.open(file_name), index_col=0).sample(frac=1)
    df.loc[df.wahlperiode == 17, 'government'] = df[df.wahlperiode == 17].partei.isin(['cducsu', 'fdp'])
    df.loc[df.wahlperiode == 18, 'government'] = df[df.wahlperiode == 18].partei.isin(['cducsu', 'spd'])
    
    return df


def assignment_08():
    df = load_data()
    X_train, X_test, y_train, y_test = train_test_split(df['text'], df['government'], test_size=0.2)
    # loading stopwords
    stopwords = [w.strip() for w in open("data/stopwords.txt").readlines()]

    text_clf = Pipeline([('vect', TfidfVectorizer(stop_words=stopwords,
                                                  max_features=int(1e5))),
                                                  ('clf', SGDClassifier(loss='log'))])

    # some hyperparameters
    parameters = {
         'vect__ngram_range': [(1, 1)],
         'clf__alpha': (np.logspace(-5, -1, 5)).tolist()
    }
    
    # perform gridsearch to get the best regularizer
    clf = GridSearchCV(text_clf, parameters, cv=2, n_jobs=1, verbose=0)
    clf.fit(X_train, y_train)

    print(classification_report(y_test, clf.predict(X_test)))

    predictions = clf.predict(df.loc[df.wahlperiode == 18, 'text'])
    print(classification_report(df.loc[df.wahlperiode == 18, 'government'], predictions))


assignment_08()
