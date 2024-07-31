import streamlit as st
import pandas as pd

data = pd.read_excel('data.xlsx')
# Set title
st.title("CSV File Uploader")

# File uploader for CSV
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the uploaded CSV file
    df = pd.read_csv(uploaded_file)
    
    # Display the DataFrame as a table
    st.write("CSV File Contents:")
    st.write(df)
else:
    st.write("Please upload a CSV file to view its contents.")

st.write(data)