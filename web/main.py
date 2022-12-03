from pytube import YouTube
from flask import *
from mp3 import mp3_download
from mp4 import mp4_download
import sys

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    print(request.form["link"])
    link = request.form.get("link")
    return render_template("home.html")

@app.route("/list/<link>")
def list_elem(link):
    stream = mp3_download(link)
    return render_template("list.html", stream=stream)

# link = input("Enter the link:")

# try:
#     yt = YouTube(link)

# except:
#     print("Invalid Link")
#     sys.exit()

# print("\nTitle: ", yt.title)
# print("Length: ", yt.length, "s")

# print("Select Download Format\n1. MP3\n2.MP4\n")
# inp = int(input())



# ##






# @app.route("/<int:celsius>")
# def fahrenheit_from(celsius):
#     """Convert Celsius to Fahrenheit degrees."""
#     fahrenheit = float(celsius) * 9 / 5 + 32
#     fahrenheit = round(fahrenheit, 3)  # Round to three decimal places
#     return str(fahrenheit)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)