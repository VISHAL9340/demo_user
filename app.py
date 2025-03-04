import streamlit as st
import yt_dlp
import os
import time

st.title("📥 Instagram Reel Downloader")

link = st.text_input("📌 Enter Instagram Reel Link:")

if st.button("🚀 Download Reel"):
    if link:
        try:
            filename = f"reel_{int(time.time())}.mp4"
            filepath = os.path.join("downloads", filename)

            ydl_opts = {
                'outtmpl': filepath,
                'format': 'bestvideo+bestaudio/best',
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
            
            with open(filepath, "rb") as file:
                st.download_button(label="📥 Click here to Download", data=file, file_name=filename, mime="video/mp4")

        except Exception as e:
            st.error(f"❌ Something went wrong: {e}")
    else:
        st.warning("⚠ Please enter a valid Instagram reel link.")
