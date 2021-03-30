import csv

"""
This file is another part of inspecting and cleaning up, 
issues with duplates prompted further inspection.
This program can be used to mess around with csv file. 
There is more information in the movie csv file but only need a couple of sections.
"""
# IMDB list for sorting out the posters
imdb_list = []

# Data cleaning from csv file 
with open("movies_metadata.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader, None) # Skip header
    line_count = 0
    count_list = []
    dup = []
    for row in csv_reader:
        if len(row) == 24:
            if line_count < 1000000:
                
                mov_id = row[5]
                imdb_id = row[6]
                # Add IMDB_id to list
                imdb_list.append(imdb_id)
                mov_title    = row[8]
                mov_overview = row[9]
                mov_lang     = row[7]
                mov_runtime  = row[16]
                mov_vote_average = row[22]
                
                
                # Multi dic to a string "/" of genres
                
                genre_data = eval(row[3])
                for gen in genre_data:
                    genre = gen['name']
                    # Add multi genres to the genre table
           

                year_data     = row[14]
                if year_data == "":
                    mov_year = "NULL"
                else:
                    mov_year = year_data.split('-')[0]
                
                
                line_count += 1
            
                # For testing purposes 
                print(line_count,mov_id)
                if mov_id not in count_list:
                    count_list.append(mov_id)
                else:
                    dup.append([mov_id, mov_title])
    #print(dup)

# Write IMDB list to csv file for checking against available posters
with open('imdb_list.csv', 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    for row in imdb_list:
        writer.writerow([row])