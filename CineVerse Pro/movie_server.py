import subprocess
import os
import random
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# --- JAVA CONNECTION ---
def get_secure_token():
    try:
        if not os.path.exists("TokenGenerator.class"):
            subprocess.run(["javac", "TokenGenerator.java"], check=False)
        result = subprocess.run(["java", "TokenGenerator"], capture_output=True, text=True)
        if result.stdout: return result.stdout.strip()
        return "JAVA_LINK_ESTABLISHED"
    except:
        return f"SECURE_SESSION_{random.randint(1000,9999)}"

# --- DATABASE (12 Movies with Full Details) ---
movies_db = [
    {"id": 1, "title": "Avatar: The Way of Water", "genre": "Sci-Fi", "year": 2022, "duration": "3h 12m", "rating": 9.7, "desc": "Jake Sully lives with his newfound family formed on the extrasolar moon Pandora.", "img": "https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg", "backdrop": "https://image.tmdb.org/t/p/original/8rpDcsfLJypbO6vREc05475qg9e.jpg", "cast": ["Sam Worthington", "Zoe Saldana", "Sigourney Weaver"]},
    {"id": 2, "title": "The Dark Knight", "genre": "Action", "year": 2008, "duration": "2h 32m", "rating": 9.5, "desc": "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham.", "img": "https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg", "backdrop": "https://image.tmdb.org/t/p/original/hkBaDkMWbLaf8B1lsWsKX7Zdt0h.jpg", "cast": ["Christian Bale", "Heath Ledger", "Aaron Eckhart"]},
    {"id": 3, "title": "La La Land", "genre": "Romance", "year": 2016, "duration": "2h 8m", "rating": 8.8, "desc": "While navigating their careers in Los Angeles, a pianist and an actress fall in love.", "img": "https://image.tmdb.org/t/p/w500/uDO8zWDhfWz7xHh9ThX704BjT.jpg", "backdrop": "https://image.tmdb.org/t/p/original/6aUWe0GSl69wMTSWWexsorMIvwU.jpg", "cast": ["Ryan Gosling", "Emma Stone", "John Legend"]},
    {"id": 4, "title": "Inception", "genre": "Sci-Fi", "year": 2010, "duration": "2h 28m", "rating": 9.2, "desc": "A thief who steals corporate secrets through the use of dream-sharing technology.", "img": "https://image.tmdb.org/t/p/w500/9gk7adHYeDvHkCSEqAvQNLV5Uge.jpg", "backdrop": "https://image.tmdb.org/t/p/original/s3TBrRGB1jav7fwNgGqnjOz601H.jpg", "cast": ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Elliot Page"]},
    {"id": 5, "title": "The Conjuring", "genre": "Horror", "year": 2013, "duration": "1h 52m", "rating": 8.9, "desc": "Paranormal investigators work to help a family terrorized by a dark presence.", "img": "https://image.tmdb.org/t/p/w500/wVYREutTvI2tmxr6ujrHT704wGF.jpg", "backdrop": "https://image.tmdb.org/t/p/original/l4eM196f7c53641C89lqT3cSA8.jpg", "cast": ["Patrick Wilson", "Vera Farmiga", "Ron Livingston"]},
    {"id": 6, "title": "Spider-Man: Across the Spider-Verse", "genre": "Animation", "year": 2023, "duration": "2h 20m", "rating": 9.6, "desc": "Miles Morales catapults across the Multiverse, where he encounters a team of Spider-People.", "img": "https://image.tmdb.org/t/p/w500/8Vt6mWEReuy4Of61Lnj5Xj704m8.jpg", "backdrop": "https://image.tmdb.org/t/p/original/4HodYYKEIsGOdinkGi2Ucz6X9i0.jpg", "cast": ["Shameik Moore", "Hailee Steinfeld", "Oscar Isaac"]},
    {"id": 7, "title": "Avengers: Endgame", "genre": "Action", "year": 2019, "duration": "3h 1m", "rating": 9.0, "desc": "After the devastating events of Infinity War, the universe is in ruins.", "img": "https://image.tmdb.org/t/p/w500/or06FN3Dka5tukK1e9sl16pB3iy.jpg", "backdrop": "https://image.tmdb.org/t/p/original/7RyHsO4yDXtBv1zUU3mTpHeQ0d5.jpg", "cast": ["Robert Downey Jr.", "Chris Evans", "Mark Ruffalo"]},
    {"id": 8, "title": "Oppenheimer", "genre": "Drama", "year": 2023, "duration": "3h", "rating": 9.4, "desc": "The story of American scientist J. Robert Oppenheimer and his role in the atomic bomb.", "img": "https://image.tmdb.org/t/p/w500/8Gxv8gSFCU0XGDykEGv7zR1n2ua.jpg", "backdrop": "https://image.tmdb.org/t/p/original/fm6KqXpk3M2HVveHwvkHIeHYDI6.jpg", "cast": ["Cillian Murphy", "Emily Blunt", "Matt Damon"]},
    {"id": 9, "title": "IT", "genre": "Horror", "year": 2017, "duration": "2h 15m", "rating": 8.0, "desc": "In the summer of 1989, a group of bullied kids band together to destroy a shape-shifting monster.", "img": "https://image.tmdb.org/t/p/w500/9E2y5Q7WlCVNEhP5GiVTjhEhx1o.jpg", "backdrop": "https://image.tmdb.org/t/p/original/tcheoA2nPATCm2vvXw2hZs4nIyD.jpg", "cast": ["Bill Skarsgård", "Jaeden Martell", "Finn Wolfhard"]},
    {"id": 10, "title": "Joker", "genre": "Drama", "year": 2019, "duration": "2h 2m", "rating": 9.1, "desc": "In Gotham City, mentally troubled comedian Arthur Fleck is disregarded and mistreated by society.", "img": "https://image.tmdb.org/t/p/w500/udDclJoHjfjb8Ekgsd4FDteOkCU.jpg", "backdrop": "https://image.tmdb.org/t/p/original/n6bUvigpRFqSwmPp1m2YADdbRBc.jpg", "cast": ["Joaquin Phoenix", "Robert De Niro", "Zazie Beetz"]},
    {"id": 11, "title": "Dune: Part Two", "genre": "Sci-Fi", "year": 2024, "duration": "2h 46m", "rating": 9.4, "desc": "Paul Atreides unites with Chani and the Fremen while on a warpath of revenge.", "img": "https://image.tmdb.org/t/p/w500/1pdfLvkbY9ohJlCjQH2CZjjYVvJ.jpg", "backdrop": "https://image.tmdb.org/t/p/original/xOMo8BRK7PfcJv9JCnx7s5hj0PX.jpg", "cast": ["Timothée Chalamet", "Zendaya", "Rebecca Ferguson"]},
    {"id": 12, "title": "Top Gun: Maverick", "genre": "Action", "year": 2022, "duration": "2h 10m", "rating": 9.3, "desc": "After thirty years, Maverick is still pushing the envelope as a top naval aviator.", "img": "https://image.tmdb.org/t/p/w500/62HCnUTziyWcpDaBO2i1DX17ljH.jpg", "backdrop": "https://image.tmdb.org/t/p/original/odJ4hx6g6vBt4lBWKFD1tI8WS4x.jpg", "cast": ["Tom Cruise", "Jennifer Connelly", "Miles Teller"]}
]

@app.context_processor
def inject_token():
    return dict(token=get_secure_token())

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/movie/<int:movie_id>')
def movie_details(movie_id):
    movie = next((m for m in movies_db if m['id'] == movie_id), None)
    if not movie:
        return "Movie not found", 404
    return render_template('movie.html', movie=movie)

@app.route('/favorites')
def favorites():
    return render_template('favorites.html')

@app.route('/api/list', methods=['GET'])
def list_movies():
    return jsonify(movies_db)

@app.route('/api/ai-filter', methods=['POST'])
def ai_filter():
    data = request.json
    user_mood = data.get('mood', '').lower()
    
    mood_map = {
        "action": ["Action", "Sci-Fi", "Animation"],
        "happy": ["Animation", "Action", "Romance"],
        "excited": ["Action", "Sci-Fi"],
        "sad": ["Romance", "Drama"],
        "scared": ["Horror", "Sci-Fi"],
        "love": ["Romance", "Drama"],
        "romantic": ["Romance", "Drama"],
        "dark": ["Horror", "Drama"],
    }

    selected_genres = []
    for mood, genres in mood_map.items():
        if mood in user_mood:
            selected_genres.extend(genres)
    
    if not selected_genres:
        return jsonify(movies_db)
    
    filtered = [m for m in movies_db if m['genre'] in selected_genres]
    unique_filtered = list({v['id']:v for v in filtered}.values())
    return jsonify(unique_filtered)

if __name__ == '__main__':
    app.run(debug=True, port=5000)