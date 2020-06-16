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

8. Käynnistä sovellus komennolla `python run.py`. Sovellus on nyt käytössä. Avaa sovellus internet-selaimella osoitteessa (http://localhost:5000/). Voit sulkea sovelluksen näppäinyhdistelmällä `Ctrl + C` tai sulkemalla komentorivin.

9. Kirjaudu sisään tunnuksella `testi` ja salasanalla `salasana`. Vaihda salasana (ja halutessasi myös muut käyttäjän tiedot) ensimmäisellä käyttökerralla yläpalkin valikon kohdasta _Asetukset_.

## Sovelluksen asennus Heroku-tilille

*Ohjeissa oletetaan, että koneellasi on käytössä [Git](https://git-scm.com/) ja [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) -työkalut. Jos näin ei ole, asenna ne ensin. Jos sinulla ei vielä ole Heroku-tunnuksia, [luo ne itsellesi](https://signup.heroku.com/) ja kirjaudu Herokuun komentoriviltä komennolla `heroku login`.*

1. Asenna sovellus ensin paikallisesti omalle tietokoneellesi yllä olevien ohjeiden kohtien 1-4 mukaisesti.

*Jos latasit sovelluksen ZIP-pakettina, luo sovellukselle ensin oma Git-repositorio komennolla `git init`.*

2. Luo Heroku-sovellus komennolla `heroku create` tai, jos haluat nimetä sovelluksen itse, komennolla `heroku create sovelluksennimi`. Ota talteen sovelluksen käyttöliittymän osoite (esim. *https://sovelluksennimi.herokuapp.com/*), sekä Git-osoite (esim. *https://git.heroku.com/sovelluksennimi.git*).

3. Lisää Git-versionhallintaan tieto herokusta komennolla `git remote add heroku https://git.heroku.com/sovelluksennimi.git`, missä loppuosa on siis kohdassa 2 talteen ottamasi Git-osoite.

4. Siirrä sovellus Herokuun suorittamalla komennot `git add .`, `git commit -m "Initial commit"` ja `git push heroku master`.

8. Sovellus on käytössä hetken kuluttua, kun Heroku on ensin ladannut sovelluksen. Avaa sovelluksen käyttöliittymä internet-selaimella kohdassa 2 talteen ottamallasi osoitteella (esim. *https://sovelluksennimi.herokuapp.com/*).