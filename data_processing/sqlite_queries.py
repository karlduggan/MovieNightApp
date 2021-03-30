
import sqlite3

"""
Will be using this file to experiement on sql queries
"""

conn = sqlite3.connect("movie_database.db")
query = """
    SELECT title, year, runtime FROM movies 
    WHERE year = '1999' 
    AND lang = 'en' 
    AND runtime < 90.0
    """
# Getting genres from id
query_genre = """
    SELECT genre FROM genres
    WHERE genre_id == 949
"""
# Getting id and title from chosen genre
query_genre2 = """
    SELECT genre_id FROM genres
    WHERE genre == "Horror"
"""

query_rating = """
    SELECT rating FROM ratings
    WHERE rate_id == 949
"""

# Joining Tables
query_join = """
    SELECT movies.title, year, rating 
    FROM movies
    LEFT JOIN ratings
    ON movies.mov_id = ratings.rate_id;
"""

query_join2 = """
    SELECT movies.mov_id
    FROM movies
    LEFT JOIN genres
    ON movies.mov_id = genres.genre_id
    WHERE genre="Comedy"
    
"""

query_year = """
    SELECT year FROM movies
    WHERE year == "2017"

"""

cursor = conn.cursor()
cursor.execute(query_join2)
data = cursor.fetchall()
res = []




"""
Each movie has multi genres in the genres table
The below will help generate a list of result.
If chosen genre links to a movie it will great a list of
mov_id's so that the relevant details can be selected afterwards

"""
# User enters the genre and a list of ids is generated as a result
def create_id_list_from_genre(genre):
    
    query_join = """
        SELECT movies.mov_id
        FROM movies
        LEFT JOIN genres
        ON movies.mov_id = genres.genre_id
        WHERE genre=?
        """
    conn = sqlite3.connect('movie_database.db')
    cur = conn.cursor()
    res = cur.execute(query_join, (genre,)).fetchall()
    result = [i[0] for i in res]
    return result

# Gets the movie data from mov_id
def _get_data_from_db(mov_id):
    query = """
        SELECT * FROM movies
        WHERE mov_id=?
    """
    conn = sqlite3.connect('movie_database.db')
    cur = conn.cursor()
    res = cur.execute(query, (mov_id,)).fetchall()
    return res[0]

# Generates a list using the _get_data_from_db functions which will be the entire result
def create_result_list_from_id(id_list):
    result = []
    for i in id_list:
        data = _get_data_from_db(i)
        result.append(data)
    return result
    