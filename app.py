import streamlit as st
import openai
import requests

# Replace with your OpenWeatherMap API key
WEATHER_API_KEY = 'your-openweathermap-api-key'
# Replace with your OpenAI API key
OPENAI_API_KEY = 'your-openai-api-key'

# Set up OpenAI API key
openai.api_key = OPENAI_API_KEY

def get_weather(city):
    """Fetch weather data from OpenWeatherMap API."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    if data.get('cod') != 200:
        return "City not found or an error occurred."

    weather_description = data['weather'][0]['description']
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    
    return f"The weather in {city} is currently {weather_description} with a temperature of {temperature}°C and humidity of {humidity}%."

def get_ai_response(prompt):
    """Get response from OpenAI's GPT-3 model."""
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text.strip()

st.title("AI Weather Query App")

st.write("Ask about the weather in any city!")

query = st.text_input("Enter your weather query:")

if st.button("Get Weather"):
    if query:
        # Generate a prompt for the AI to handle the query
        prompt = f"Extract the city name from this query and provide the weather information for the city: {query}"
        ai_response = get_ai_response(prompt)
        
        # Assuming the AI response contains the city name
        city_name = ai_response
        weather_info = get_weather(city_name)
        st.write(weather_info)
    else:
        st.warning("Please enter a query.")
