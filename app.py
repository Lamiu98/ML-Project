import streamlit as st
import openai

# Replace with your own OpenAI API key
openai.api_key = 'your-openai-api-key'

st.title("AI Text Generator")

st.write("This is a simple AI text generation app using OpenAI's GPT-3 model.")

# Input from the user
prompt = st.text_area("Enter a prompt for the AI to continue:")

if st.button("Generate Text"):
    if prompt:
        with st.spinner('Generating...'):
            # Generate the text using OpenAI's API
            response = openai.Completion.create(
                engine="text-davinci-003",  # Use the appropriate model
                prompt=prompt,
                max_tokens=150
            )
            generated_text = response.choices[0].text.strip()
            st.write("### Generated Text")
            st.write(generated_text)
    else:
        st.warning("Please enter a prompt.")

st.write("Powered by Streamlit and OpenAI")
