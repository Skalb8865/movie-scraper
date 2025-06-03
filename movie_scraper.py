from flask import Blueprint, request, render_template

import requests

movie_scraper = Blueprint("movie_scraper", __name__)

@movie_scraper.route("/", methods=["GET", "POST"])
def home():
    movie_data = None
    if request.method == "POST":
        text = request.form["text"]
        movie_data = fetch_movie_data(text)
    return render_template("index.html", movie_data=movie_data)

def fetch_movie_data(title):
    url = f"http://www.omdbapi.com/?apikey=259c7947&t={title}"
    response = requests.get(url)
    return response.json()



@movie_scraper.route("/json", methods=["GET", "POST"])
def json():
    movie_data = None
    if request.method == "POST":
        text = request.form["text"]
        movie_data = fetch_movie_data(text)
        return movie_data
    return render_template("json.html", movie_data=movie_data)