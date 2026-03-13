from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "2b054ec6549477dae6ef2db2bd55ad09"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/results")
def results():
    movie = request.args.get("movie")
    
    url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie}"
    response = requests.get(url)
    data = response.json()
    
    movies = data["results"]
    
    return render_template("results.html", movie=movie, movies=movies)

if __name__ == "__main__":
    app.run()