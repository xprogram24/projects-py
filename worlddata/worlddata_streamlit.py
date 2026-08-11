import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🌍 World Population Dashboard")
st.write("Scraped live from Worldometers using BeautifulSoup and Pandas.")

# Load data
df = pd.read_csv("worldometers_population.csv")

# Show raw data checkbox
if st.checkbox("Show Raw Data Table"):
    st.dataframe(df)

# Simple Plot

# Option A: Built-in Streamlit Line Chart (Interactive with zero configuration)
st.subheader("Population Trend Over Time")
st.line_chart(df, x='Year (July 1)', y='Population')
