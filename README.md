
# BeeFlower

BeeFlower on peli, jossa pelataan Betty Mehiläisellä. Mehiläisen tehtävä on kerätä 20 kukkaa, mutta varoa osumasta pisaroihin. Peli menee haastavammaksi, mitä enemmän kukkia on kerännyt.

## Dokumentaatio

- [Vaatimusmäärittely](https://github.com/AinoKruth/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)

- [Työaikakirjanpitoon](https://github.com/AinoKruth/ot-harjoitustyo/blob/main/dokumentaatio/tyoaikakirjanpito.md)

- [Changelog](https://github.com/AinoKruth/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)

- [Release](https://github.com/AinoKruth/ot-harjoitustyo/releases/tag/viikko5)

## Asennus
1. Asenna pelin riippuvuudet komennolla:
```bash
poetry install
```
2. Suorita pelin vaadittavat alustustoimenpiteet komennolla:
```bash
poetry run ivoke build
```
3. Käynnistä peli komennolla:
```bash
poetry run invoke start
```

## Komentorivitoiminnot

Ohjelman suorittaminen:
```bash 
poetry run invoke start
```
Ohjelman testaus:
```bash 
poetry run invoke test
```
Ohjelman testikattavuus:
```bash 
poery run invoke coverage-report
```
Ohjelman pylint tarkastukset:
```bash 
poetry run invoke lint
```
