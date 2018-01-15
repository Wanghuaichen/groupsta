# Technisch ontwerp

## Controllers
- /register
  - POST
  - def register():
    - Account aanmaken

- /login
  - POST
  - def login():
    - Gebruikers naam en wachtwoord invoeren. Session id opslaan

- /index
  - GET en POST
  - login required
  - def index():
    - Main feed ophalen (GET)
    - Group feed ophalen (GET)
    - Lijst van groepen ophalen (GET)
    - Account gegevens ophalen (GET)
    - Zoekfunctie (POST)
    - Liken (POST)
    - Commenten en Gif (POST/GET)
