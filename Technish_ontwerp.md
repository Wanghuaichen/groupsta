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

- /index
  - GET en POST
  - login required
  - def index():
    - Main feed ophalen (GET)
    - Groupfeed ophalen (GET)
    - Lijst van groepen ophalen / navigatie (GET)
      - instellingen
      - groepen
      - post pagina
    - Account gegevens ophalen (GET)
    - Zoekfunctie (POST)
    - Liken (POST)
    - Commenten en Gif (POST/GET)

- /groupfeed
  - GET en POST
  - login required
  - def groupfeed():
    - Groupdata ophalen (GET)
      - aantal leden, feed, beschrijving etc
    - Lijst van groepen ophalen / navigatie (GET)
    - Account gegevens ophalen (GET)
    - Zoekfunctie (POST)
    - Liken (POST)
    - Commenten en Gif (POST/GET)

- /post
  - GET en POST
  - login required
  - def post():
    - Lijst van groepen ophalen en dan dropdown menu om keuze te maken in welke groep je wilt plaatsen (GET / POST)
    - Foto kunnen uploaden van je computer (POST)
    - caption voor bij je foto (POST)
    - Lijst van groepen ophalen / navigatie (GET)
    - Account gegevens ophalen (GET)
    - Zoekfunctie (POST)
    
- /settings
  - GET en POST
  - login required
  - def settings():
    - Lijst van groepen ophalen / navigatie (GET)
    - Account gegevens ophalen (GET)
    - Zoekfunctie (POST)
    - Profielfoto veranderfunctie (POST)
    - Wachtwoord veranderfunctie (POST)
    - Emailadres wijzigen (POST)
    - Gebruikersnaam veranderen (POST)
  
