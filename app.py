import streamlit as st
import pandas as pd

st.title("Excel File Reader, Hoang Lam")
st.markdown("_Prototype v0.4.1_")

@st.cache_data
def load_data(path:str):
    data = pd.read_excel(path)
    return data

df = load_data("./data.xlsx")
with st.expander("Data preview"):
    st.dataframe(df)