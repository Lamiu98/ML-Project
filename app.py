import streamlit as st
import pandas as pd

st.title("Excel File Reader")

# Upload Excel file
uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx"])

if uploaded_file is not None:
    # Read the Excel file into a DataFrame
    df = pd.read_excel(uploaded_file, engine='openpyxl')

    # Display the DataFrame
    st.write("### Data from the Excel file:")
    st.write(df)

    # Optionally, you can add more functionality like data analysis or plotting
    # For example, showing basic statistics:
    st.write("### Basic Statistics:")
    st.write(df.describe())
    
    # For additional functionality like displaying specific sheets or columns
    sheet_names = pd.ExcelFile(uploaded_file, engine='openpyxl').sheet_names
    st.write("### Sheet names:")
    st.write(sheet_names)
    
    # Optionally, let the user select which sheet to display
    sheet_name = st.selectbox("Select sheet", sheet_names)
    df_sheet = pd.read_excel(uploaded_file, sheet_name=sheet_name, engine='openpyxl')
    st.write(f"### Data from the sheet: {sheet_name}")
    st.write(df_sheet)
else:
    st.write("Upload an Excel file to see the data.")
