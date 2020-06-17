# Käyttöohje

## Sovelluksen käynnistäminen

1. Avaa sovellus selaimella osoitteessa [https://tsoha-sopimuskanta.herokuapp.com/]. Vaihtoehtoisesti voit asentaa sovelluksen omalle koneellesi [asennusohjeiden](https://github.com/teemuoksanen/tsoha-sopimuskanta/documentation/Installation.md) mukaisesti.

2. Kirjaudu sisään ikkunan oikeassa yläkulmassa olevasta _Kirjaudu sisään_ -linkistä.

3. Kirjautumisen jälkeen näet etusivulla, mikäli sinulla on tekemättömiä muistutuksia, joiden määräpäivä on täynnä.

*Jos sinulla ei vielä ole omia tunnuksia, voit luoda kirjautumalla ensin sisään tunnuksella *testi* ja salasanalla *salasana*. Voit luoda uudet tunnukset kohdasta 'Käyttäjät -> Lisää uusi käyttäjä'. Normaalikäytössä ylläpitäjä luo käyttäjille tunnukset.*

## Sopimukset

### Sopimuksien selaaminen ja hakeminen

Valitse yläpalkista _Sopimukset_ --> _Listaa sopimukset_ taikka suoraan etusivulta _Listaa sopimukset_. Kaikki sopimukset on listattu sivulle allekirjoituspäivän mukaisessa järjestyksessä vanhimmasta uusimpaan.

Halutessasi voit hakea sopimuksia hakusanalla avaamalla _Hae ja suodata sopimuksia_ -ikkunan. Haku kohdistuu sopimusten nimiin, ja voit hakea mitä tahansa merkkijonoa. Samasta ikkunasta voit valita myös, että listauksessa näytetään vain omat sopimukset ja/tai voimassa olevat sopimukset. Jos haluat esimerkiksi näyttää kaikki omat sopimuksesi, jätä hakusana tyhjäksi ja valitse _Näytä vain omat sopimukset_. Päivitä sopimuslista painamalla _Hae sopimukset_.

Voit nollata hakusanat ja suodattimet ja palata kaikkien sopimusten näyttöön painamalla _Nollaa suodattimet_.

### Yksittäisen sopimuksen tietojen katselu

Yksittäisen sopimuksen tietosivun saat auki painamalla sopimuksen nimeä sopimuslistauksessa. Vaihtoehtoisesti pääset sopimuksen tietosivulle myös esimerkiksi osapuolen tiedoista tai muistutuksesta.

Sopimuksesta näytetään sille lisätyt osapuolet, allekirjoitus-, voimaantulo- ja umpeutumispäivämäärät sekä tieto sopimuksen tämänhetkisestä voimassaolosta.

Sopimuksen tietosivulla näkyy myös toimintoina muistutuksen lisääminen sekä sopimuksen omistajalle ja ylläpitäjille sopimuksen muokkaaminen ja poistaminen.

### Sopimuksen lisääminen

Valitse yläpalkista _Sopimukset_ --> _Lisää uusi sopimus_ taikka suoraan etusivulta _Lisää uusi sopimus_. Anna sopimuksen otsikko tai muu kuvaava nimi _Sopimuksen nimi_ -kenttään. Valitse ainakin sopimuksen allekirjoitus- ja voimaantulopäivät sekä umpeutumispäivä, mikäli sellainen on. Jos sopimus on toistaiseksi voimassa oleva, jätä umpeutumispäivä tyhjäksi. Päivämäärän voit valita päivämääräketän oikean reunan nuolesta aukeavasta kalenterista tai syöttää sen muodossa _pp.kk.vvvv_.

Jos asetat sopimukselle umpeutumispäivän, sopimuksen omistajalle lisätään automaattisesti muistutus sopimuksen umpeutumispäivälle.

Ylläpitäjä voi valita myös käyttäjän, joka merkitään sopimuksen omistajaksi. Sopimuksen omistaja voi esimerkiksi muokata sopimuksen tietoja, vaikka ei olisi ylläpitäjä. Kun tavallinen käyttäjä lisää sopimuksen, sopimuksen omistajaksi merkitään automaattisesti kyseinen käyttäjä.

Sopimukselle voi lisätä osapuolia sopimuksen tietosivulta seuraavan kohdan mukaisesti sen jälkeen, kun olet ensin lisännyt sopimuksen.

### Osapuolen lisääminen sopimukselle ja poistaminen sopimukselta

Avaa sopimuksen tietosivu esimerkiksi sopimuslistasta. Valitse _Osapuolet_-tietolaatikon alalaidasta *Lisää osapuoli sopimukselle*. Valitse lisättävä osapuoli luettelosta ja paina *Lisää*. Voit myös hakea osapuolia luettelon yläreunan hakukentästä. Jos osapuolta ei löydy listalta, voit siirtyä osapuolen lisäämissivulla painamalla *Luo uusi osapuoli*.

Voit lisätä sopimukselle kuinka monta osapuolta tahansa. Lisääminen tapahtuu yksi osapuoli kerrallaan.

Huomaathan, että *Lisää osapuoli sopimukselle* -ikkunassa ei näytetä sellaisia osapuolia, jotka on jo aiemmin lisätty sopimukselle.

### Sopimuksen tietojen muokkaaminen

Avaa sopimuksen tietosivu esimerkiksi sopimuslistasta. Valitse _Toiminnot_-laatikosta _Muokkaa sopimusta_. Huomaathan, että muokkauspainiketta ei näy, jos et ole sopimuksen omistaja tai ylläpitäjä.

Jos lisäät sopimukselle umpeutumispäivän, sopimuksen omistajalle lisätään automaattisesti muistutus sopimuksen umpeutumispäivälle. Huomaathan, että aiemmin tehtyjä automaattisia muistutuksia ei poisteta, mikäli muutat umpeutumispäivää tai poistat sen kokonaan.

### Sopimuksen poistaminen

Avaa sopimuksen tietosivu esimerkiksi sopimuslistasta. Valitse _Toiminnot_-laatikosta _Poista sopimus_ ja vahvista poistaminen painamalla _Poista_. Huomaathan, että poistamispainiketta ei näy, jos et ole sopimuksen omistaja tai ylläpitäjä.

Kun poistat sopimuksen, se poistetaan lopullisesti eikä sitä voi enää palauttaa. Samalla poistetaan kaikki sopimukseen liittyvät aiemmin luodut muistutukset.

## Osapuolet

### Osapuolten selaaminen ja hakeminen

Valitse yläpalkista _Osapuolet_ --> _Listaa osapuolet_ taikka suoraan etusivulta _Listaa osapuolet_. Osapuolet on listattu sivulle aakkosjärjestyksessä. Konkurssissa olevat osapuolet on merkitty punaisella taustavärillä.

Halutessasi voit hakea sopimuksia hakusanalla avaamalla _Hae osapuolia_ -ikkunan. Haku kohdistuu osapuolten nimiin, ja voit hakea mitä tahansa merkkijonoa. Päivitä osapuolilista painamalla _Hae osapuolet_. Voit nollata hakusanat ja palata kaikkien osapuolten näyttöön painamalla _Nollaa suodattimet_.

### Yksittäisen osapuolen tietojen katselu

Yksittäisen osapuolen tietosivun saat auki painamalla osapuolen nimeä osapuolilistauksessa. Vaihtoehtoisesti pääset osapuolen tietosivulle myös esimerkiksi sopimuksen tiedoista.

Osapuolesta näytetään sen nimi, Y-tunnus ja osoite sekä siihen liitetyt sopimukset.

Osapuolen tietosivulla näkyy myös toimintoina osapuolen muokkaaminen, konkurssiin asettaminen ja poistaminen.

### Osapuolen lisääminen

Valitse yläpalkista _Osapuolet_ --> _Lisää uusi osapuoli_ taikka suoraan etusivulta _Lisää uusi osapuoli_. Anna osapuolen nimi, Y-tunnus sekä osoitetiedot.

### Osapuolen asettaminen konkurssiin ja konkurssitiedon peruuttaminen

Avaa osapuolen tietosivu esimerkiksi osapuolilistasta. Valitse _Toiminnot_-laatikosta _Aseta konkurssiin_ ja vahvista konkurssiin asettaminen vahvistusikkunassa painamalla _Aseta konkurssiin_. Konkurssitieto näytetään punaisella varoitusvärillä ja _"Konkurssissa"_-merkinnällä niissä yhteyksissä, missä osapuoleen viitataan. Jokaiselle käyttäjälle, jonka sopimuksiin kyseinen osapuoli on liitetty, tehdään automaattisesti aktiivinen muistutus, jossa kehotetaan tarkistamaan mahdolliset toimenpiteet konkurssin takia.

Voit myös poistaa konkurssitiedon osapuolen tietosivulta. Valitse _Toiminnot_-laatikosta _Poista konkurssitieto_ ja vahvista konkurssitiedon poistaminen vahvistusikkunassa painamalla _Poista konkurssitieto_. Aiemmin lisättyjä konkurssimuistutuksia ei tässä yhteydessä poisteta.

### Osapuolen tietojen muokkaaminen

Avaa osapuolen tietosivu esimerkiksi osapuolilistasta. Valitse _Toiminnot_-laatikosta _Muokkaa osapuolta_.

### Osapuolen poistaminen

Avaa osapuolen tietosivu esimerkiksi osapuolilistasta. Valitse _Toiminnot_-laatikosta _Poista osapuoli_ ja vahvista poistaminen painamalla _Poista_. Mikäli osapuoli on liitettynä johonkin sopimukseen, poistaminen ei kuitenkaan ole mahdollista. Poista osapuoli ensin jokaiselta siihen liittyvältä sopimukselta, ja poista osapuoli vasta tämän jälkeen.

Kun poistat osapuolen, se poistetaan lopullisesti eikä sitä voi enää palauttaa.

### Tilastoja osapuolista

Valitse yläpalkista _Osapuolet_ --> _Tilastoja osapuolista_ taikka suoraan etusivulta _Tilastoja osapuolista_. Tilastosivulta näet osapuolten sekä konkurssissa olevien osapuolten lukumäärät. Tilastosivulta näet lisäksi (enintään) viisi osapuolta, joilla on eniten sopimuksia, sekä (enintään) viisi osapuolta, joilla on eniten voimassa olevia sopimuksia. Näet myös kootusti osapuolet, joilla ei ole vielä yhtään sopimusta.

## Muistutukset

### Muistusten selaaminen ja kuittaaminen tehdyksi

Etusivulla näet, mikäli sinulla on tekemättömiä muistutuksia, joiden määräpäivä on täynnä. Voit siirtyä muistutukseen liittyvään sopimukseen painamalla sopimuksen nimeä. Voit kuitata muistutuksen tehdyksi painamalla _Merkitse tehdyksi_. Tehdyksi kuitattu muistutus poistuu automaattisesti etusivulta.

Kaikki muistutuksesi näet valitsemalla yläpalkista _Muistutukset_ --> _Listaa muistutukset_ taikka suoraan etusivulta _Muistutuksiin_. Muistutuksesi on listattu sivulle niiden määräpäivän mukaisessa järjestyksessä - ylemmässä listauksessa on tekemättömät muistutukset. Halutessasi voit selata myös tehtyjä muistutuksiasi avaamalla _Tehdyt muistutukset_-ikkunan sen otsikkoa painamalla.

Voit kuitata muistutuksen tehdyksi painamalla muistutuksen perässä _Tehty_-sarakkeessa olevaa laatikon kuvaa. Tehdyksi kuitattu muistutus siirretään _Tehdyt muistutukset_-ikkunaan.

Halutessasi voit palauttaa muistutuksen tekemättömiin muistutuksiin painamalla _Tehdyt muistutukset_-ikkunassa muistutuksen perässä _Tehty_-sarakkeessa olevaa valitun laatikon kuvaa. Tällöin muistutuksen tekokuittaus nollataan ja muistutus siirretään takaisin tekemättömien muistutusten listalle ja mahdollisesti myös etusivun aktiivisten muistutusten listaan.

### Muistutuksen lisääminen

Valitse yläpalkista _Muistutukset_ --> _Lisää uusi muistutus_. Vaihtoehtoisesti voit luoda muistuksen valitsemalla _Lisää muistutus_ yksittäisen sopimuksen tietosivulla.

Kirjoita muistutusteksti ja valitse muistutuspäivä. Päivämäärän voit valita päivämääräketän oikean reunan nuolesta aukeavasta kalenterista tai syöttää sen muodossa _pp.kk.vvvv_. Muistutuspäivänä ja sen jälkeen kyseinen muistutus näytetään käyttäjän etusivulla, jos kyseistä muistutusta ei vielä ole kuitattu tehdyksi.

Valitse myös listalta sopimus, johon muistutus liittyy. Jos lisäät muistutusta sopimuksen tietosivun kautta, kyseinen sopimus on valmiiksi valittuna. Voit myös hakea sopimuksia luettelon yläreunan hakukentästä.

Ylläpitäjä voi valita myös käyttäjän, jolle muistutus lisätään. Kun tavallinen käyttäjä lisää muistutuksen, muistutus lisätään aina hänelle itselleen.

### Muistutuksen tietojen muokkaaminen

Voit muokata muistutusta menemällä muistutuslistaan valitsemalla yläpalkista _Muistutukset_ --> _Listaa muistutukset_. Paina muistutuksen perässä olevaa kynän kuvaa, niin pääset muokkaamaan muistutuksen tietoja.

### Muistutuksen poistaminen

Voit poistaa muistutuksen menemällä ensin muistutuslistaan valitsemalla yläpalkista _Muistutukset_ --> _Listaa muistutukset_. Paina muistutuksen perässä olevaa kynän kuvaa. Valitse muistutuksen muokkaussivulla _Poista muistutus_ ja vahvista poistaminen painamalla _Poista_.

Kun poistat muistutuksen, se poistetaan lopullisesti eikä sitä voi enää palauttaa.

### Muistutusten hallinta ylläpitäjänä

Ylläpitäjä voi halutessaan tarkastella, muokata ja kuitata tehdyksi kaikkien käyttäjien muistutuksia. Valitse yläpalkista _Muistutukset_ --> _Listaa muistutukset_ ja paina sen jälkeen otsikon vieressä olevaa keltaista _Näytä kaikkien käyttäjien muistutukset_-painiketta. Avautuvalla sivulla näkyvät kaikkien käyttäjien muistutukset. Toiminnot vastaavat muilta osin yllä olevia muistutuksiin liittyviä toimintoja.

Ylläpitäjä voi palata omiin muistutuksiinsa painamalla otsikon vieressä olevaa keltaista _Näytä vain omat muistutukset_-painiketta.

## Omat asetukset

Valitsemalla yläpalkista _Asetukset_ voit muokata omaa nimeäsi, käyttäjätunnustasi sekä salasanaasi.

## Käyttäjien hallinta (vain ylläpitäjät)

### Käyttäjän lisääminen

Valitse yläpalkista _Käyttäjät_ --> _Lisää uusi käyttäjä_. Anna käyttäjän nimi, käyttäjätunnus, salasana (kahdesti) sekä käyttäjätyyppi (Käyttäjä tai Ylläpitäjä).

### Käyttäjien listaaminen ja muokkaaminen

Valitse yläpalkista _Käyttäjät_ --> _Listaa käyttäjät_. Käyttäjät on listattu sivulle tunnuksen mukaisesti aakkosjärjestyksessä. Jokaisen käyttäjän kohdalla näkyy myös kyseiseen käyttäjään liittyvien sopimusten määrä.

Käyttäjän tietoja (nimi ja tunnus) sekä salasanaa voit muokata painamalla käyttäjän perässä olevaa kynän kuvaa.

Käyttäjän poistaminen ei ole toistaiseksi mahdollista. Halutessasi voit esimerkiksi muuttaa käyttäjän salasanan niin, että hän ei enää pääse kirjautumaan sovellukseen.