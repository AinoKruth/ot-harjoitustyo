## Käyttöohje

Lataa viimeisin release lähdekoodi Assets-osion alta Source code.

## Ohjelman käynnistäminen

Ennen kuin käynnistät pelin, asenna riippuvuudet komennolla:

```bash
poetry install
```
Suorita sitten alustustoimepiteet:
```bash
poetry run ivoke build
```
Ja käynnistä peli komennolla:
```bash
poetry run invoke start
```
## Pelin toiminnot

Pelin käynnistyessä, tulee esiin alkuteksti, joka selittää pelin tarkoituksen.
Tästä pääsee peliin enteriä painamalla.

Pelin hahmoa ohjataan nuolinäppäimillä, ja jos pelin haluaa laittaa pauselle, se toimii painalla p-näppäintä.
Jos taas halua jatkaa peliä, pitää painaa c-näppäintä.

Jos häviät pelin, tai pääset sen läpi voit aloittaa uuden pelin painamalla n näppäintä. Jos taas haluat poistua
pelistä, onnistuu se painamalla esc-näppäintä.
