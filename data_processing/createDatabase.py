import sqlite3

class DatabaseGenerator:
    def __init__(self, database_name):
        self.database = database_name
    
    def create_connection(self):
        conn = None
        try: 
            conn = sqlite3.connect(self.database)
            return conn
        except Error as e:
            print(e)
    
    def createTable_movies(self):
        query = """
            CREATE TABLE movies (
                mov_id INTEGER PRIMARY KEY,
                title TEXT,
                lang TEXT,
                year TEXT,
                overview TEXT,
                runtime FLOAT,
                image TEXT
            )"""

        conn = self.create_connection()
        c = conn.cursor()
        c.execute(query)
        conn.commit()
    
    def createTable_genres(self):
        query = """
                CREATE TABLE genres (
                    genre_id INTERGER,
                    title TEXT,
                    genre TEXT
                )
                """
        conn = self.create_connection()
        c = conn.cursor()
        c.execute(query)
        conn.commit()

    def createTable_ratings(self):
        query = """
                CREATE TABLE ratings (
                    rate_id INTERGER,
                    title TEXT,
                    rating FLOAT
                )
                """
        conn = self.create_connection()
        c = conn.cursor()
        c.execute(query)
        conn.commit()
        
    # Adding new movie to the movie table
    def add_movie(self, mov_id, title, lang, year, overview, runtime, image):
        query = """
                INSERT INTO movies (mov_id, title, lang, year, overview, runtime, image)
                VALUES(?,?,?,?,?,?,?)
                """
        conn = self.create_connection()
        c = conn.cursor()
        c.execute(query, (mov_id, title, lang, year, overview, runtime, image))
        conn.commit()
    
    # Adding new movie genres to the genre table
    def add_movie_genre(self, genre_id, mov_title, genre):
        query = """
                INSERT INTO genres (genre_id, title, genre)
                VALUES(?,?,?)
                """
        conn = self.create_connection()
        c = conn.cursor()
        c.execute(query, (genre_id, mov_title, genre))
        conn.commit()

    # Adding new movie rating to the ratings table
    def add_movie_rating(self, rate_id, mov_title, rating):
        query = """
                INSERT INTO ratings (rate_id, title, rating)
                VALUES(?,?,?)
                """
        conn = self.create_connection()
        c = conn.cursor()
        c.execute(query, (rate_id, mov_title, rating))
        conn.commit()

if __name__ == "__main__":
    db = DatabaseGenerator("movie.db")
  
