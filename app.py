import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import streamlit as st
import pickle

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

st.set_page_config(page_title="Sentiment Analysis")

st.title("Sentiment Analysis of Amazon Alexa Reviews")
st.write("Enter a review to predict sentiment")

review = st.text_area("Customer Review")

if st.button("Predict Sentiment"):
    if review.strip() == "":
        st.warning("Please enter a review")
    else:
        review_vector = vectorizer.transform([review])
        prediction = model.predict(review_vector)

        if prediction[0] == 0:
            st.success("Positive Review 😊")
        else:
            st.error("Negative Review ☹️")
