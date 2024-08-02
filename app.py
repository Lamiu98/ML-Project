import streamlit as st
from utils import PrepProcess, colu
import pandas as pd

st.title("Excel File Reader, Hoang Lam")
st.markdown("_Prototype v0.4.1_")


df = pd.read_excel ("./data.xlsx")
st.dataframe(df)