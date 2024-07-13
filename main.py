import streamlit as st
import plotly.express as px

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")


def get_data(days):
    dates = ["2024-07-10","2024-07-11", "2024-07-12", "2024-07-13"]
    temperatures = [10,20,3,40]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures


d, t = get_data(3)

figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)