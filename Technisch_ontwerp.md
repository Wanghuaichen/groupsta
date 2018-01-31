# Technisch ontwerp

## Controllers
- /register
  - POST
  - def register():
    - Account aanmaken
      - gebruikersnaam, wachtwoord, email

- /login
  - POST
  - def login():
    - Gebruikers naam en wachtwoord invoeren. Session id opslaan

- /logout
    - def logout():
        - Gebruiker uitloggen

- /index
  - GET en POST
  - login required
  - def index():
    - Main feed ophalen (GET)
    - Groupfeed ophalen (GET)
    - Lijst van groepen ophalen / navigatie (GET/POST)
      - instellingen
      - groepen
      - post pagina
      - zoekfunctie
    - Liken (POST)
    - Commenten en Gif (POST/GET)
    
- /<group_name>
  - def group(group_name):
  - Verlengde van /index waarbij specifieke feed van groep enkel wordt geladen

- /post
  - GET en POST
  - login required
  - def post():
    - Lijst van groepen ophalen en dan dropdown menu om keuze te maken in welke groep je wilt plaatsen (GET / POST)
    - Foto kunnen uploaden van je computer (POST)
    - caption voor bij je foto (POST)
    - Lijst van groepen ophalen / navigatie (GET/POST)
      - instellingen
      - groepen
      - post pagina
      - zoekfunctie

- /settings
  - GET en POST
  - login required
  - def settings():
    - Lijst van groepen ophalen / navigatie (GET/POST)
      - instellingen
      - groepen
      - post pagina
      - zoekfunctie
    - Account gegevens ophalen (GET)
      - gebruikersnaam
      - wachtwoord
    - Wachtwoord veranderfunctie (POST)
    - Gebruikersnaam veranderen (POST)

- /profile
  - GET en POST
  - login required
  - def profile():
    - Lijst van groepen ophalen / navigatie (GET)
      - instellingen
      - groepen
      - post pagina
      - zoekfunctie
    - Liken (POST)
    - Commenten en Gif (POST/GET)
    - Persoonlijke feed (GET)

- /create
  - GET en POST
  - login required
  - def create():
    - Lijst van groepen ophalen / navigatie (GET/POST)
      - instellingen
      - groepen
      - post pagina
      - zoekfunctie
    - Groep aanmaken functie (POST)
      - Naam
      - Beschrijving
      - Groepsavatar (Hoort niet bij MVP)

- /followgroup
    - GET en POST
    - login required
    - Lijst van groepen ophalen / navigatie (GET/POST)
      - instellingen
      - groepen
      - post pagina
      - zoekfunctie
    - Lijst van groepen die je kan volgen
    - Knop waarmee je kan volgen
  
  - /livesearch
    - geimplementeerde livesearch functie

- /admin (Hoort niet bij MVP)
  - GET en POST
  - login required
  - admin status required
  - def admin():
    - Lijst van groepen ophalen / navigatie (GET/POST)
      - instellingen
      - groepen
      - post pagina
      - zoekfunctie
    - Groupdata ophalen (GET)
      - aantal leden, feed, beschrijving, etc
      - extra: lijst van leden
    - Gebruiker verwijderen uit groep (POST)
    - Groepdata aanpassen (POST)
      - Naam, beschrijving
    - Groep verwijderen (POST)

- /explore (Hoort niet bij MVP)
  - GET en POST
  - Login required
  - def explore():
    - Lijst van groepen ophalen / navigatie (GET)
      - instellingen
      - groepen
      - post pagina
      - zoekfunctie
    - Liken (POST)
    - Commenten en Gif (POST/GET)
    - Random feed ophalen (GET)

## Views
![My image](https://github.com/Zjoerdie/UvAgram/blob/master/pictures/prototype_website.jpg?raw=true "hoi")

## Models/helper

Helper:
- Login required functie

Models:
- Users
  - Register
  - Login
  - Change password
  - Change username
  - Profile feed
- Groups
  - Create
  - Follow
  - Explore groups
  - Load all groups
  - Load all posts of a group
  - Groupinfo
  - Name to group_id converter
  - Followed
  - Main feed
  - Follow check
- Posts
  - Upload
  - Load groups followed by user
  - Comment text
  - Comment Gif
  - Load comments
  - Like

## Plugins in framework
- Flask
  - http://flask.pocoo.org/
- Bootstrap
  - https://getbootstrap.com/docs/4.0/getting-started/download/
- phpmyadmin
  - https://www.phpmyadmin.net/
- Giphy API
  - http://api.giphy.com
- Safygiphy API Wrapper
  - https://github.com/StewPoll/safygiphy
- Flask-uploads API
  - https://pythonhosted.org/Flask-Uploads/
  - https://github.com/maxcountryman/flask-uploads
- AJAX | jQuery API
  - http://api.jquery.com/jquery.ajax/
