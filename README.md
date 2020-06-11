# Sopimuskanta

Sopimuskantaan voi tallentaa tietoja sopimuksista sekä niiden osapuolista. Sopimuksen omistajaksi merkitään ensisijaisesti käyttäjä, joka on lisännyt sopimuksen järjestelmään, mutta omistajaa voi myös vaihtaa. Sopimukseen voi liittää käyttäjäkohtaisia muistutuksia, jotka näkyvät asetettuna päivämääränä kyseiselle käyttäjälle. Osa muistutuksista voidaan luoda automaattisesti (esim. umpeutuva sopimus, konkurssiin mennyt osapuoli).

Kullekin käyttäjälle voidaan antaa joko luku- taikka luku- ja kirjoitusoikeudet. Lukuoikeudet omaava ei voi lisätä sopimuksia, mutta voi lisätä muistutuksia itselleen. Kirjoitusoikeuden omaavat voivat lisätä muistutuksia myös muille. Ylläpitäjäksi merkitty käyttäjä voi luoda myös uusia käyttäjiä.

## Sovellus Herokussa

Sovellus löytyy osoitteesta (https://tsoha-sopimuskanta.herokuapp.com/).

Ylläpitäjän oikeuksilla olevat tunnukset testikäyttöä varten:
- Tunnus: __'testi'__
- Salasana: __'salasana'__

Voit luoda uuden käyttäjän kirjautumalla ensin sisään yllä olevilla tunnuksilla.

## Dokumentaatio

- [Käyttäjätarinat ja SQL-kyselyt](https://github.com/teemuoksanen/tsoha-sopimuskanta/blob/master/documentation/UserStories.md)

- [Sovelluksen asennusohje](https://github.com/teemuoksanen/tsoha-sopimuskanta/blob/master/documentation/Installation.md)

- [Sovelluksen käyttöohje](https://github.com/teemuoksanen/tsoha-sopimuskanta/blob/master/documentation/Manual.md)

## Alustava tietokantakaavio

![Tietokantakaavio](https://github.com/teemuoksanen/tsoha-sopimuskanta/blob/master/documentation/pics/tietokantakaavio.png)

- [Tietokantakaavio](https://github.com/teemuoksanen/tsoha-sopimuskanta/blob/master/documentation/pics/tietokantakaavio.png)

- [Tekstimuotoinen tietokantakuvaus](https://github.com/teemuoksanen/tsoha-sopimuskanta/blob/master/documentation/DatabaseDescription.md)