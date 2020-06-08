# Sovelluksen asennus

## Sovelluksen asennus paikallisesti omalle tietokoneelle

1. Lataa sovelluksen tiedostot GitHub-repositoriosta (https://github.com/sonjaheikkinen/lintuhavainnot/archive/master.zip).

2. Pura ladattu ZIP-paketti haluamaasi kansioon.

3. Avaa tietokoneen komentorivi ja siirry kansioon, johon purit ZIP-paketin. Kansion nimi on oletuksena *tsoha-sopimuskanta-master*.

4. Luo Python-virtuaaliympäristö kyseiseen kansioon komennolla `python3 -m venv venv`.
​
5. Ota Python-virtuaaliympäristö käyttöön komennolla `source venv/bin/activate`. Komentorivin vasemmassa laidassa näkyy virtuaaliympäristön tunnisteena teksti `(venv)`.

6. Asenna sovelluksen vaatimat riippuvuudet komennolla `pip install -r requirements.txt`.

7. Käynnistä sovellus komennolla `python run.py`. Sovellus tulee käynnistää Pyhton-virtuaaliympäristössä - ota se tarvittaessa ensin käyttöön komennolla `source venv/bin/activate`.

8. Sovellus on nyt käytössä. Avaa sovellus internet-selaimella osoitteessa *[http://localhost:5000/]*. Voit sulkea sovelluksen näppäinyhdistelmällä `Ctrl + C` tai sulkemalla komentorivin. 

## Sovelluksen asennus Heroku-tilille

(KESKEN)