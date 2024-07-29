import glob
import streamlit as st
import plotly.express as px
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

filepaths = sorted(glob.glob("diary/*.txt"))

neativity = []
postivity = []

for filepath in filepaths:
    with open(filepath) as file:
        content = file.read()
        results = analyzer.polarity_scores(content)
        postivity.append(results["pos"])
        neativity.append(results["neg"])

dates = [name.strip(".txt").strip("diary/") for name in filepaths]

st.title("Mood Tracker")
st.subheader("Postivity")
pos_figure = px.line(x=dates, y=postivity,labels={"x":"Date", "y":"Postivity"})
st.plotly_chart(pos_figure)

st.subheader("Negativity")
px.line(x=dates, y=neativity,labels={"x":"Date", "y":"Negativity"})
st.plotly_chart(pos_figure)
