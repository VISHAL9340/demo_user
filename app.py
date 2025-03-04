from flask import Flask, render_template, request, send_file
import yt_dlp
import os
import time

app = Flask(__name__)

DOWNLOAD_FOLDER = "static/downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        link = request.form["url"]
        if link:
            try:
                filename = f"reel_{int(time.time())}.mp4"
                filepath = os.path.join(DOWNLOAD_FOLDER, filename)

                ydl_opts = {
                    'outtmpl': filepath,
                    'format': 'bestvideo+bestaudio/best',
                }

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([link])

                return send_file(filepath, as_attachment=True)
            
            except Exception as e:
                return f"Error: {e}"

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
