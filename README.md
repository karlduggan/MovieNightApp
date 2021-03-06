# Movie Night App (In Progress)

**Movie Database.**

Tired of wasting time flicking through Netflix's and Primes ? MovieNight will help you find your next movie by generating a top 10 list from from films you haven't seen before. Movie Night is a quick and simple solution to solve this problem, once the user has there own account they will be able to click a recommendation button that will recommend a movie that matches there liking.

* **30,000+ Movie Database** - MovieNight has a database with 30,000+ titles to explore through.

**Task Completion List**
* **Build Movie Database** - 30,000+ titles
* **Build an API** - 


## Requirements

Python 3.8.5+, pipenv

## Instalation

First, clone this repository.

    $ git clone http://github.com/karlduggan/MovieNightApp
    $ cd MovieNightApp

After, install all necessary to run:

    $ pipenv install

Than, run the application:

  $ pipenv run python run.py

To see your application, access this url in your browser: 

  http://localhost:5000
  
## Progress Entries

31/03/2021 - Flip cards added along with 5 star rating component 
<br/>
<img src="progress_01.png">
<br/>

03/04/2021 - Update to flip cards along with 5 star and half star rating component.
Added:
*  Bookmark (to the top right corner) - not connected yet to a system
*  Border around back of card
*  Director (no data for that yet)
*  Year and runtime inline 
*  Overview text scrollable 
*  Overlay (front of card) dims when hover   
<br/>
<img src="card_update_02.png">
<br/>

05/04/2021 - Created search and nav bar.
Added:
*  Search bar added and connect to fetch api to movies
*  Nav bar added
<br/>
<img src="progress_03.png">
<br/>

10/04/2021 - Focused on redisigning components communication and lazy loading
Added:
*  Layout responsive and some designs adjusted
*  Genre dropdown added and connected ( using custom event listeners )
*  Lazy loading movie cards created ( each component has its own fetch request and takes only an ID attribute )
*  load in component created ( Communicates via an event listener and fetches users request )

## Known Issues:
    * Database needs redisgning, dividing the main movie table into separate tables 
    * New tables needed - Actors, Directors, Writers and ratings ( Rotten Tomato, Imdb, Metacritic )  
<br/>
<img src="progress_04.png">
<br/>
