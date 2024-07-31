import streamlit as st

# Set the title of the app
st.title("Data Input App")

# Input fields
name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=0)
email = st.text_input("Enter your email:")

# Button to submit the data
if st.button("Submit"):
    if name and age and email:
        # Display the entered data
        st.write("Name:", name)
        st.write("Age:", age)
        st.write("Email:", email)
    else:
        st.write("Please fill in all fields in table.")