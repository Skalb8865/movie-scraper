from flask import Flask
from movie_scraper import movie_scraper

app = Flask(__name__)
app.register_blueprint(movie_scraper, url_prefix="/")

if __name__ == '__main__':
    app.run(debug=True, port=8000)