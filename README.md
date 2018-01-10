# Groupsta
Instagram maar dan met groepen.

## Samenvatting
Het idee achter Groupsta zijn de groepen, je deelt de foto niet met je volgers zoals bij Instagram maar binnen één van je communities om groepen mensen weer met elkaar in contact te brengen. De nadruk bij Groupsta ligt bij de comments onder de foto's. Communities kunnen simpel gemaakt worden en een community mag overal over gaan, denk bijvoorbeeld aan een sportvereniging, vriendengroep, evenement of bijvoorbeeld een bejaardentehuis. Als iemand een foto plaatst in zo’n groep kan iedereen die lid is van die groep het bekijken/liken/delen of reageren.

## Schetsen
Schetsen staan in Slackkanaal.

## Features
- Foto's posten
- Groepen aanmaken (groepsbeheer)
- Groepen volgen
- Comments plaatsen (text of gif)
- Foto's liken
- Foto's delen/posten
- Notificaties
- Account instellingen
- Zoekfunctie
- Foto's bekijken (main feed)

## Potentiële extra features
- Upvote systeem
- Privé groep
- Groepsbeheer
  - mensen uit groepen verwijderen
  - beschrijving groep aanpassen
- Evenementenfunctie

## Minimal viable product
- Foto's posten
- Foto's bekijken
- Comments plaatsen (inclusief gifs)
- Account instellingen (simpel)
- Groepen volgen
- Groepen aanmaken (zonder groepsbeheer)

## Afhankelijkheden

### Databronnen
- Giphy API
  - http://api.giphy.com

### Externe componenten
- Flask
  - http://flask.pocoo.org/
- Bootstrap (potentieël)
  - https://getbootstrap.com/docs/4.0/getting-started/download/ 
- phpmyadmin
  - https://www.phpmyadmin.net/

### Concurrerende bestaande websites
- Instagram
  - Ons project is gebaseerd op Instagram, bijna alle basisfuncties van deze applicatie worden overgenomen.
- Reddit
  - Reddit werkt met subreddits (communities), en op deze subreddits kan je abboneren. Wij gaan het subreddit idee implementeren in onze applicatie door middel van de groepen functie.

### Moeilijkste delen
- Zoekmachine is moeilijk te implementeren.
- Database goed inrichten.
- Groepenfunctie implementeren.
