import flask
from flask import request, jsonify, render_template
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d



@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/api/v1/resources/movies/all', methods=['GET'])
def api_all():
    # Connect to movie database
    conn = sqlite3.connect('app/movie_database.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_movies = cur.execute('SELECT * FROM movies;').fetchall()

    return jsonify(all_movies)
    
    
@app.route('/api/v1/resources/movies', methods=['GET'])
def api_filter():
    """
    Example for Filtering in the parameters
    /api/v1/resources/movies?lang=en&year=1999
    """
    query_parameters = request.args
    id = query_parameters.get('id')
    title = query_parameters.get('title')
    genre = query_parameters.get('genre')
    year = query_parameters.get('year')
    lang = query_parameters.get('lang')
    limit = query_parameters.get('limit')
    
    # The correct query template needs to be selected depending if genre is part of the parameter
    query = None
    
    query_genre = """
        SELECT *
        FROM movies
        LEFT JOIN genres
        ON movies.mov_id = genres.genre_id 
        WHERE
    """
    query_none = """
        SELECT *
        FROM movies
        WHERE
    """
    if genre:
        query = query_genre
    else:
        query = query_none
        
        
    to_filter = []

    if id:
        query += ' mov_id=? AND'
        to_filter.append(id)
    if title:
        query += ' title LIKE ? AND'
        # The wild card % will allow a wider search for words that appear in title
        to_filter.append('%'+ title +'%')
    if year:
        query += ' year=? AND'
        to_filter.append(year)
    if lang:
        query += ' lang=? AND'
        to_filter.append(lang)
    if genre:
        query += ' genre=? AND'
        to_filter.append(genre)

        
    if not (id or title or genre or year):
        return page_not_found(404)

    
    query = query[:-4] + ';'

    conn = sqlite3.connect('app/movie_database.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()
    
    # Check if a limit is set in the parameter
    result_with_limit = []
    if limit:
        limit = int(limit)
        # If the limit is greater than the actual result then just return the result
        if  len(results) > limit:
            for i in range(limit):
                result_with_limit.append(results[i])
            return jsonify(result_with_limit)
        
    # If no limit then return the complete result 
    return jsonify(results)



