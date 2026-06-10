# app.py

import pandas as pd
import string

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

faq = pd.read_csv("faq.csv")

questions = faq["Question"].tolist()
answers = faq["Answer"].tolist()

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess(text):
    text = text.lower()

    tokens = word_tokenize(text)

    tokens = [
        word for word in tokens
        if word not in string.punctuation
    ]

    tokens = [
        word for word in tokens
        if word not in stop_words
    ]

    tokens = [
        lemmatizer.lemmatize(word)
        for word in tokens
    ]

    return " ".join(tokens)

processed_questions = [
    preprocess(question)
    for question in questions
]

vectorizer = TfidfVectorizer()
faq_vectors = vectorizer.fit_transform(processed_questions)

def get_best_answer(user_query):

    processed_query = preprocess(user_query)

    query_vector = vectorizer.transform([processed_query])

    similarity_scores = cosine_similarity(
        query_vector,
        faq_vectors
    )

    best_match_index = similarity_scores.argmax()

    confidence = similarity_scores[0][best_match_index]

    if confidence < 0.2:
        return "Sorry, I don't understand that question."

    return answers[best_match_index]