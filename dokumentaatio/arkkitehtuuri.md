# Arkkitehtuurikuvaus

## Rakenne

Koodin pakkausrakenne näyttää seuraavalta:
![image](https://github.com/AinoKruth/ot-harjoitustyo/assets/128384992/af809e60-7b48-4a23-b244-228991450032)

Main sisältää pelin loopin koodin, events pakkauksesta löytyy pelin sovelluslogiikan koodi, bee taas pitää sisällään
mehiläisen liikkumisesta vastaavan koodin, keys:stä löytyy näppäinten koodin ja draw pakkauksessa on kaikki grafiikkaan liittyvä koodi. 
Picturesissa oleva koodi lataa kuvat peliin.

## Sovelluslogiikka

Eventa pakkauksessa tapahtuu kaikki sovelluslogiikkaan liittyvä. Funktiot new_game, game_passed, game_end ja paused,
asettaa uuden pelin arvot kohdilleen, tarkistaa onko peli päästy läpi ja onko peli loppunut/hävitty. Sen lisäksi 
tietysti pausettaa pelin kun pelaaja niin haluaa. 
Tämän lisäksi pelin käynnissä ollessa see_event tarkistaa aikaisemmin mainitut fuktiot, ja jos peli on käynnissä siirtyy flower_waterdrop
funktioon, jossa määritellään mistä kohtaa ja mikä leveli on menossa, eli miten nopeasti kukat ja pisarat tippuvat.

## Toiminnallisuus

Alla olevan sekvenssikaavio näyttää pelin toiminnallisuutta

![image](https://github.com/AinoKruth/ot-harjoitustyo/assets/128384992/8b7afa08-a9dc-4835-9b7d-d37923897645)

Kun peli käynnistetään main tiedostosta se aloittaa piirtämällä aloitustekstin draw.py:ssä. Sen jälkeen se asettaa arvot uudelle pelille eventsissä kunnes palaa takaisin mainiin.
Tässä vaiheessa main aloittaa loopin, jossa se aloittaa piirtämällä näytön, hakemalla kuvat pictures.py:stä. Eventsissä se hakee
näppäimistön toiminnan keys.py:stä ja mehiläisen liikumisen parametrit bee.py:stä kunnes palaa takaisin mainin looppiin tarkistamaan tapahtumia.

Loopissa se palaa eventsiin tarkistamaan tapahtumia ja reagoi niiden tarvitsemalla tavalla. Näin tapahtuu niin pitkään kunnes pelaaja lopettaa pelaamisen.

