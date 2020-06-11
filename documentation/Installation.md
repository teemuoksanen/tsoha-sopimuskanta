# Sovelluksen asennus

## Sovelluksen asennus paikallisesti omalle tietokoneelle


1. Avaa tietokoneen komentorivi ja siirry kansioon, johon haluat asentaa sovelluksen. Hae sovelluksen koodi GitHubista komennolla `git clone https://github.com/teemuoksanen/tsoha-sopimuskanta.git`.

*Vaihtoehtoisesti voit ladata tiedostot GitHub-repositoriosta [ZIP-pakettina](https://github.com/teemuoksanen/tsoha-sopimuskanta/archive/master.zip). Pura ladattu ZIP-paketti haluamaasi kansioon. Avaa sen jälkeen tietokoneen komentorivi.*

2. Siirry kansioon komennolla *cd tsoha-sopimuskanta*. (Jos hait sovelluksen ZIP-pakettina, hakemiston nimi on todennäköisesti *tsoha-sopimuskanta-master*.)

4. Luo Python-virtuaaliympäristö kyseiseen kansioon komennolla `python3 -m venv venv`.
​
5. Ota Python-virtuaaliympäristö käyttöön komennolla `source venv/bin/activate`. Komentorivin vasemmassa laidassa näkyy virtuaaliympäristön tunnisteena teksti `(venv)`.

6. Asenna sovelluksen vaatimat riippuvuudet komennolla `pip install -r requirements.txt`.

7. Käynnistä sovellus komennolla `python run.py`. Sovellus tulee käynnistää Pyhton-virtuaaliympäristössä - ota se tarvittaessa ensin käyttöön komennolla `source venv/bin/activate`.

8. Sovellus on nyt käytössä. Avaa sovellus internet-selaimella osoitteessa *[http://localhost:5000/]*. Voit sulkea sovelluksen näppäinyhdistelmällä `Ctrl + C` tai sulkemalla komentorivin. 

## Sovelluksen asennus Heroku-tilille

(KESKEN)
