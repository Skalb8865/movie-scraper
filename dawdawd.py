import requests

def fetch_movie_data(title):
    url = f"http://www.omdbapi.com/?i=tt3896198&apikey=259c7947&t={title}"
    response = requests.get(url)
    return response.json()
    
movie_data = fetch_movie_data("Avatar")
print(movie_data)