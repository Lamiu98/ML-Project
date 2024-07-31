import streamlit as st
import pandas as pd
import os

# Set title
st.title("Excel File Viewer")

# Define the path to the folder containing Excel files
folder_path = 'data.xlsx'  # Replace with the path to your folder

# List all Excel files in the folder
excel_files = [f for f in os.listdir(folder_path) if f.endswith(('.xlsx', '.xls'))]

# Select file from dropdown
selected_file = st.selectbox("Select an Excel file", excel_files)

if selected_file:
    # Construct full file path
    file_path = os.path.join(folder_path, selected_file)
    
    # Read the selected Excel file
    df = pd.read_excel(file_path)
    
    # Display the DataFrame as a table
    st.write(f"Contents of {selected_file}:")
    st.write(df)
else:
    st.write("Please select an Excel file to view its contents.")
