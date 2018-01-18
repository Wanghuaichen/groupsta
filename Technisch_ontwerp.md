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

- /groupfeed
  - GET en POST
  - login required
  - def groupfeed():
    - Groupdata ophalen (GET)
      - aantal leden, feed, beschrijving, etc
    - Lijst van groepen ophalen / navigatie (GET/POST)
      - instellingen
      - groepen
      - post pagina
      - zoekfunctie
    - Liken (POST)
    - Commenten en Gif (POST/GET)

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
      - email
    - Profielfoto veranderfunctie (POST)
    - Wachtwoord veranderfunctie (POST)
    - Emailadres wijzigen (POST)
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
- Apology functie
  - Functie die aangeeft als er ergens een error is
- Zoekfunctie in database
  - Functie om in database te zoeken naar een bepaald iets (Groep)
- Feed laden
  - een functie die de database aanroept en de feed van bijvoorbeeld een groep ophaalt
- Random feed laden
  - willekeurige feed ophalen

## Plugins in framework
- Flask
  - http://flask.pocoo.org/
- Bootstrap (potentieël)
  - https://getbootstrap.com/docs/4.0/getting-started/download/
- phpmyadmin
  - https://www.phpmyadmin.net/
- Giphy API
  - http://api.giphy.com
- Wordt wellicht nog aangevuld met meer API's
