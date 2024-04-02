# Import necessary libraries
import streamlit as st
import speech_recognition as sr

# Set page title
st.title("Speech-to-Text Converter")

# Create a function to convert speech to text
def speech_to_text(language='en-US'):
    # Create instance of Recognizer
    recognizer = sr.Recognizer()

    # Use microphone as audio source
    with sr.Microphone() as source:
        st.write("Speak something...")
        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source)
        # Listen for user input
        audio = recognizer.listen(source)
        try:
            st.write("Transcription:")
            # Use recognize_google method to transcribe speech
            text = recognizer.recognize_google(audio, language=language)
            # Display transcribed text
            st.write(text)
        except sr.UnknownValueError:
            st.write("Sorry, couldn't understand audio.")
        except sr.RequestError as e:
            st.write(f"Request error: {e}")

# Create sidebar for customization options
st.sidebar.title("Settings")
language = st.sidebar.selectbox("Select Language", ['en-US', 'es-ES'])

# Call speech_to_text function when button is clicked
if st.button("Start Recording"):
    speech_to_text(language)
