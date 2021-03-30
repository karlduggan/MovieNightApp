import csv
from createDatabase import DatabaseGenerator

# Create database
database = DatabaseGenerator("movie_database.db")

# Movie general info
database.createTable_movies()

# Movie genre table
database.createTable_genres()

# Movies ratings table
database.createTable_ratings()

# Data cleaning from csv file 
with open("movies_metadata.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader, None) # Skip header
    line_count = 0
    file_list = []
    duplicate = []
    for row in csv_reader:
        if len(row) == 24:
            if line_count < 1000000:
                
                mov_id = row[5]
                imdb_id = row[6]
                mov_title    = row[8]
                mov_overview = row[9]
                mov_lang     = row[7]
                mov_runtime  = row[16]
                mov_vote_average = row[22]
                
                # Check for duplicates
                if mov_id not in file_list:
                    file_list.append(mov_id)
                    
                    genre_data = eval(row[3])
                    for gen in genre_data:
                        genre = gen['name']
                        # Add multi genres to the genre table
                        database.add_movie_genre(mov_id, mov_title, genre)

                    year_data     = row[14]
                    if year_data == "":
                        mov_year = "NULL"
                    else:
                        mov_year = year_data.split('-')[0]
                    
                    # Add movie to the database
                    database.add_movie(mov_id, mov_title, mov_lang, mov_year, mov_overview, mov_runtime, "NA")
                    
                    # Add movie rating
                    database.add_movie_rating(mov_id, mov_title, mov_vote_average)
                
                # IF movie id already in file list add to duplicate
                else:
                    duplicate.append(mov_id)
                
                line_count += 1
                
                # For checking progress while the program runs
                print(line_count)
                
    print(f"The number of duplicate files: {len(duplicate)}")