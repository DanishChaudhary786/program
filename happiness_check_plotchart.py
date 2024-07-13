import streamlit as st
import pandas as pd
import plotly.express as px


def option_match_csv(option):
    match option:
        case "GDP":
            return "gdp"
        case "Happiness":
            return "happiness"
        case "Generosity":
            return "generosity"


df = pd.read_csv("happy.csv")

st.title("In search of Happiness")
x_axis_choice = st.selectbox("Select the data for X axis", ("GDP","Happiness","Generosity"))
y_axis_choice = st.selectbox("Select the data for Y axis", ("GDP","Happiness","Generosity"))

st.title(f"{x_axis_choice} and {y_axis_choice}")


fig = px.scatter(x=df[option_match_csv(x_axis_choice)], y=df[option_match_csv(y_axis_choice)], labels={"x": x_axis_choice, "y": y_axis_choice})
st.plotly_chart(fig)