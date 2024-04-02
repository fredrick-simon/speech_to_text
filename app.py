import streamlit as st
from streamlit_webrtc import webrtc_streamer
import speech_recognition as sr

def transcribe_audio(audio_data):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_data) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "Sorry, couldn't understand the audio"
    except sr.RequestError:
        return "Speech recognition service unavailable"

def main():
    st.title("Live Speech-to-Text")
    webrtc_ctx = webrtc_streamer(
        key="speech-to-text",
        audio_receiver_size=1024,
        desired_playing_speed=1,
        media_stream_constraints={"audio": True},
        run_button_label="Start",
    )
    if webrtc_ctx.audio_receiver:
        audio_data = webrtc_ctx.audio_receiver.value
        if st.button("Transcribe"):
            if audio_data is not None:
                st.write("Transcription in progress...")
                text = transcribe_audio(audio_data)
                st.write("Transcription:")
                st.write(text)

if __name__ == "__main__":
    main()
