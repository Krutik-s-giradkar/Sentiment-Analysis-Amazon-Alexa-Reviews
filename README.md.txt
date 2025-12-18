# Sentiment Analysis of Amazon Alexa Reviews

## ?? Project Overview
This project performs sentiment analysis on Amazon Alexa customer reviews using
Natural Language Processing (NLP) and Machine Learning techniques.
A simple web application is developed to predict whether a review is
**Positive** or **Negative**.

---

## ?? Problem Statement
Online customer reviews contain valuable information about product quality
and user satisfaction. However, manual analysis of thousands of reviews
is inefficient. This project aims to automatically classify Amazon Alexa
reviews into positive and negative sentiments using machine learning.

---

## ?? Dataset Description
- **Source:** Public Kaggle Dataset
- **Total Records:** ~3,000 reviews
- **File Format:** CSV

### Features:
- `review` – Customer review text
- `rating` – Star rating (1–5)
- `feedback` – Sentiment label  
  - 1 = Positive  
  - 0 = Negative  

---

## ??? Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Natural Language Processing (NLP)
- TF-IDF Vectorizer
- Logistic Regression
- Streamlit

---

## ?? Machine Learning Models
- Naïve Bayes
- Logistic Regression (Best Performing Model)

---

## ?? Project Workflow
1. Load dataset
2. Clean and preprocess text data
3. Convert text into numerical features using TF-IDF
4. Train machine learning models
5. Evaluate model performance
6. Save trained model and vectorizer
7. Build and run a Streamlit web application

---

## ?? Web Application
The Streamlit web app allows users to:
- Enter a customer review
- Predict sentiment instantly
- View results in a simple user interface

---

## ?? How to Run the Project
1. Clone the repository:
```bash
git clone https://github.com/Krutik-s-giradkar/Sentiment-Analysis-Amazon-Alexa-Review.git

