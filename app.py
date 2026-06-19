import os
import subprocess
import streamlit as st
import imageio_ffmpeg

# -------------------------
# Page setup
# -------------------------

st.set_page_config(
    page_title="Video Audio Player",
    page_icon="🎵",
    layout="centered"
)

st.title("🎵 Video Audio Player")
st.write("Upload a video and listen to its audio.")

# -------------------------
# Temp folder
# -------------------------

TEMP_FOLDER = "temp"
os.makedirs(TEMP_FOLDER, exist_ok=True)

# -------------------------
# Upload
# -------------------------

uploaded_video = st.file_uploader(
    "Choose a video",
    type=["mp4", "mov", "avi", "mkv", "webm"]
)

if uploaded_video:

    video_path = os.path.join(TEMP_FOLDER, uploaded_video.name)

    with open(video_path, "wb") as f:
        f.write(uploaded_video.read())

    st.success("Video uploaded!")

    st.video(video_path)

    audio_path = os.path.join(TEMP_FOLDER, "audio.mp3")

    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()

    with st.spinner("Extracting audio..."):

        result = subprocess.run(
            [
                ffmpeg,
                "-y",
                "-i", video_path,
                "-vn",
                "-acodec", "libmp3lame",
                audio_path
            ],
            capture_output=True,
            text=True
        )

    if result.returncode == 0:

        st.success("Audio extracted!")

        st.audio(audio_path)

    else:

        st.error("FFmpeg failed.")

        st.code(result.stderr)
