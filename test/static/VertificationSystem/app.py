import streamlit as st
import whisper


st.title("Whisper App")

audio_file=st.file_uploader("Upload Audio" , type=["wav","mp3","m4a"])


model=whisper.load_model("base")
st.text("Whisper model loaded")


if st.sidebar.button("Transcribe Audio"):
    if audio_file is not None:
        st.sidebar.success("Transcribing Audio")
        print(audio_file.name)
        transcription=model.transcribe(audio_file.name)
        st.sidebar.success("Transcribing Audio")
        st.text(transcription["text"])
    else:
        st.sidebar.error("Please upload an audio file")
st.sidebar.header("Play Original audio file")
st.sidebar.audio(audio_file)