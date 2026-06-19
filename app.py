import os
import streamlit as st
from moviepy.video.io.VideoFileClip import VideoFileClip

# -------------------------
# Page Setup
# -------------------------

st.set_page_config(
    page_title="Video Audio Player",
    page_icon="🎵",
    layout="centered"
)

st.title("🎵 Video Audio Player")
st.write("Upload a video and listen to its audio.")

# -------------------------
# Create temp folder
# -------------------------

os.makedirs("temp", exist_ok=True)

# -------------------------
# Upload Video
# -------------------------

video = st.file_uploader(
    "Choose a video",
    type=["mp4", "mov", "avi", "mkv", "webm"]
)

if video is not None:

    video_path = os.path.join("temp", "video.mp4")

    with open(video_path, "wb") as f:
        f.write(video.read())

    st.success("Video uploaded!")

    st.video(video_path)

    if st.button("🎵 Extract Audio"):

        with st.spinner("Extracting audio..."):

            clip = VideoFileClip(video_path)

            audio_path = os.path.join("temp", "audio.mp3")

            clip.audio.write_audiofile(
                audio_path,
                logger=None
            )

            clip.close()

        st.success("Done!")

        st.audio(audio_path)
