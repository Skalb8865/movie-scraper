from flask import Blueprint, request, render_template, redirect, url_for
import requests

movie_scraper = Blueprint(__name__, "movie_scraper")

@movie_scraper.route("/")
def home():
    return render_template("index.html")

@movie_scraper.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    def fetch_movie_data(text):
        url = f"http://www.omdbapi.com/?i=tt3896198&apikey=259c7947&t={text}"
        response = requests.get(url)
        return response.json()
        
    movie_data = fetch_movie_data("Final Destination: Bloodlines")
    return movie_data