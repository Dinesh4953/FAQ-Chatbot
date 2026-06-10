# FAQ Chatbot using NLP

## Project Overview

This project is a simple FAQ Chatbot developed using Natural Language Processing (NLP) techniques and Streamlit. The chatbot allows users to ask questions and retrieves the most relevant answer from a predefined FAQ dataset.

The project demonstrates text preprocessing, vectorization, similarity matching, and chatbot interaction through a web-based interface.

---

## Features

* Interactive chatbot interface using Streamlit
* FAQ dataset stored in CSV format
* Text preprocessing using NLTK
* Tokenization
* Stopword removal
* Lemmatization
* TF-IDF Vectorization
* Cosine Similarity for question matching
* Automatic response generation based on the closest FAQ

---

## Technologies Used

* Python
* Pandas
* NLTK
* Scikit-Learn
* Streamlit

---

## Project Structure

```text
FAQ_Chatbot/
│
├── faq.csv
├── app.py
├── chatbot.py
├── README.md
```

---

## NLP Pipeline

### 1. Data Collection

A dataset containing Frequently Asked Questions (FAQs) and their corresponding answers is stored in `faq.csv`.

### 2. Text Preprocessing

The user query and FAQ questions are processed using:

* Lowercasing
* Tokenization
* Punctuation Removal
* Stopword Removal
* Lemmatization

### 3. Vectorization

The processed text is converted into numerical vectors using TF-IDF (Term Frequency–Inverse Document Frequency).

### 4. Similarity Matching

Cosine Similarity is used to compare the user question with all FAQ questions.

### 5. Response Generation

The chatbot returns the answer corresponding to the question with the highest similarity score.

---

## Installation

### Step 1: Clone or Download the Project

```bash
git clone <repository-url>
```

### Step 2: Install Required Libraries

```bash
pip install pandas nltk scikit-learn streamlit
```

### Step 3: Download NLTK Resources

Run the following once:

```python
import nltk

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
```

---

## Running the Application

Open a terminal and execute:

```bash
streamlit run chatbot.py
```

The chatbot interface will open automatically in your browser.

---

## Example Questions

* What is Python?
* What is Machine Learning?
* What is Artificial Intelligence?
* What is NLP?
* What is Django?
* What is Streamlit?
* What is GitHub?
* What is Cloud Computing?

---

## Expected Output

User enters a question in the Streamlit interface.

Example:

```text
User: What is Python?

Bot: Python is a high-level, interpreted programming language known for its simplicity and readability. It supports object-oriented, procedural, and functional programming paradigms.
```

---

## Future Enhancements

* Voice-based chatbot interaction
* Integration with Large Language Models (LLMs)
* Semantic Search using Sentence Transformers
* Database-driven FAQ management
* Multi-language support
* Chat history storage

---

## Learning Outcomes

Through this project, the following concepts are demonstrated:

* Natural Language Processing (NLP)
* Text Cleaning and Preprocessing
* TF-IDF Vectorization
* Cosine Similarity
* Information Retrieval
* Streamlit Web Application Development
* Python-based Chatbot Development

---

## Conclusion

This project successfully implements a FAQ Chatbot using NLP techniques. It provides quick and relevant answers by matching user queries with predefined FAQs and demonstrates practical applications of text preprocessing and information retrieval.
