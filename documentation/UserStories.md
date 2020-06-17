# Käyttäjätarinat

Käyttäjätarinoiden (_user story_) perässä oleva numero viittaa dokumentin lopussa oleviin SQL-kyselyihin.

## Käyttäjänä voin...
- [x] ...listata kaikki sopimukset sekä osapuolet. _(1d)_
- [x] ...listata vain omat ja/tai voimassa olevat sopimukset. _(2d)_
- [x] ...hakea yksittäistä sopimusta. _(2d)_
- [x] ...katsoa yksittäisen sopimuksen tietoja niin, että myös sopimukseen liitetyt osapuolet listataan. _(2c)_
- [x] ...katsoa yksittäisen osapuolten tietoja niin, että myös osapuoleen liitetyt sopimukset listataan. _(3a)_
- [x] ...lisätä uusia sopimuksia (jolloin minut merkitään sopimuksen omistajaksi), osapuolia sekä sopimuksiin liittyviä muistutuksia. _(1a)_
- [x] ...muokata omistamieni sopimusten tietoja tai poistaa kyseiset sopimukset. _(1b, 1c)_
- [x] ...muokata tai poistaa omia muistutuksiani. _(1b, 1c)_
- [x] ...muokata kaikkien osapuolten tietoja. _(1b)_
- [x] ...muokata omia tietojani ja vaihtaa salasanaani. _(1b)_
- [x] ...lisätä osapuolia sopimuksiin. _(2a, 2b)_
- [x] ...listata kaikki omat muistutukseni. _(4b)_
- [x] ...nähdä etusivulla toimenpiteitä vaativat muistutukseni. _(4c)_
- [x] ...listata osapuolet, joilla on eniten sopimuksia ja eniten voimassa olevia sopimuksia, sekä osapuolet, joilla ei ole yhtään sopimusta. _(3b)_

## Ylläpitäjänä voin lisäksi...
- [x] ...luoda uusia käyttäjiä. _(1a)_
- [x] ...listata kaikki käyttäjät niin, että näen samalla, montako sopimusta kullakin käyttäjällä on. _(5a)_
- [x] ...poistaa minkä tahansa sopimuksen, osapuolen (jos osapuoli ei ole aktiivisena jollain sopimuksella) tai muistutuksen. _(1c)_
- [x] ...muokata mitä tahansa sopimusta, muistutusta tai käyttäjää. _(1b)_
- [x] ...listata kaikkien käyttäjien muistutukset. _(4a)_
- [x] ...lisätä muistutuksia kaikille käyttäjille. _(1a)_

## Yleisiä käyttötapauksia
- [x] Jos sopimukselle lisätään päättymispäivä, sopimuksen omistajalle lisätään muistutus. _(1a)_
- [x] Jos osapuoli asetetaan konkurssiin, kaikille osapuolten sopimusten omistajille lisätään muistutus. _(4d)_

# SQL-kyselyt

## 1. Yleiset

Tässä osiossa on yleisesti käytetyt, yksinkertaiset SQL-kyselyt toteutettuna sopimuksille - ne toimivat kuitenkin vastaavalla tavalla kaikille tauluille. Erityisemmät käyttötapaukset on listattu tyyppikohtaisesti.

### 1a. Kohteen lisääminen

```
INSERT INTO Contract
    (name, date_signed, date_entry, date_expiry, account_id)
    VALUES (?, ?, ?, ?, ?);
```

### 1b. Kohteen muokkaaminen

```
UPDATE Contract
    SET name = ?, date_signed = ?, date_entry = ?, date_expiry = ?, account_id = ?
    WHERE id = ?;
```

### 1c. Kohteen poistaminen

```
DELETE FROM Contract
    WHERE id = ?;
```

### 1d. Kaikkien kohteiden listaaminen

```
SELECT * FROM Contract;
```

## 2. Sopimukset

### 2a. Niiden osapuolten listaaminen, joita ei ole liitetty sopimukseen

Tätä kyselyä käytetään _Lisää osapuoli sopimukselle_-lomakkeella. Lomakkeella ei tällöin näytetä niitä osapuolia, jotka on jo liitetty sopimukselle.

```
SELECT Party.id, Party.name FROM Party
    LEFT JOIN ContractParty ON Party.id = ContractParty.party_id
    WHERE Party.id NOT IN
    (SELECT party_id FROM ContractParty WHERE contract_id = ?)
    GROUP BY Party.id;
```

### 2b. Osapuolen lisääminen sopimukselle

Osapuoli lisätään sopimukselle liitostaulun avulla. Liitostalussa _contract_id_ viittaa sopimuksen id-numeroon ja _party_id_ osapuolen id-numeroon.

```
INSERT INTO ContractParty
    (contract_id, party_id)
    VALUES (?, ?);
```

### 2c. Sopimukseen liittyvien osapuolten listaaminen

Osapuoli liitetään sopimuksen tietoihin liitostaulun avulla. Liitostalussa _contract_id_ viittaa sopimuksen id-numeroon ja _party_id_ osapuolen id-numeroon.

```
SELECT Party.id, Party.name FROM Party
    JOIN ContractParty ON Party.id = ContractParty.party_id
    WHERE ContractParty.contract_id IS ?;
```

### 2d. Sopimuksiin tehtävät haut

SQL-kyselyllä voi hakea sopimuksia nimeen kohdistuvan hakusanan perusteella. Lisäksi on mahdollista suodattaa vain tietyn käyttäjän omistamat sopimukset sekä vain voimassa olevat sopimukset. Jos haku halutaan kohdistaa kaikkiin sopimuksiin, voi jälkimmäiset AND-rivit siis jättää pois.

```
SELECT * FROM Contract
    WHERE upper(name) LIKE ?
    AND account_id = ?
    AND date_entry <= ? AND (date_expiry IS NULL OR date_expiry >= ?);
```

## 3. Osapuolet

### 3a. Osapuoleen liittyvien sopimusten listaaminen

Osapuoli liitetään sopimuksen tietoihin liitostaulun avulla. Liitostalussa _contract_id_ viittaa sopimuksen id-numeroon ja _party_id_ osapuolen id-numeroon.

```
SELECT Contract.id, Contract.name FROM Contract
    JOIN ContractParty ON Contract.id = ContractParty.contract_id
    WHERE ContractParty.party_id IS ?;
```

### 3b. Osapuolet, joilla on eniten sopimuksia tai ei yhtään sopimusta

Viisi osapuolta, joilla on eniten sopimuksia (vähintään 1):

```
SELECT Party.id, Party.name, COUNT(Contract.id) FROM Party
    JOIN ContractParty ON ContractParty.party_id = Party.id
    JOIN Contract ON ContractParty.contract_id = Contract.id
    GROUP BY Party.id
    HAVING COUNT(Contract.id) > 0
    ORDER BY COUNT(Contract.id) DESC LIMIT 5;
```

Viisi osapuolta, joilla on eniten voimassa olevia sopimuksia:

```
SELECT Party.id, Party.name, COUNT(Contract.id) FROM Party
    JOIN ContractParty ON ContractParty.party_id = Party.id
    JOIN Contract ON ContractParty.contract_id = Contract.id
    WHERE Contract.date_entry <= :today AND (Contract.date_expiry IS NULL OR Contract.date_expiry >= :today)
    GROUP BY Party.id
    ORDER BY COUNT(Contract.id) ASC LIMIT 5;
```

Osapuolet, joilla ei ole ollenkaan sopimuksia:

```
SELECT Party.id, Party.name, COUNT(Contract.id) FROM Party
    LEFT JOIN ContractParty ON ContractParty.party_id = Party.id
    LEFT JOIN Contract ON ContractParty.contract_id = Contract.id
    GROUP BY Party.id
    HAVING COUNT(Contract.id) = 0;
```

## 4. Muistutukset

### 4a. Kaikkien tekemättömien/tehtyjen muistutusten listaaminen

Jos viimeisellä rivillä on _FALSE_, haetaan tekemättömät muistutukset. Jos viimeisellä tivillä on _TRUE_, haetaan tehdyt muistutukset.

```
SELECT Reminder.id, Reminder.note, Reminder.date_remind, Reminder.done, Contract.id, Contract.name, Account.id, Account.username, Account.name FROM Reminder
    JOIN Account ON Reminder.account_id = Account.id
    JOIN Contract ON Reminder.contract_id = Contract.id
    WHERE Reminder.done = FALSE/TRUE;
```

### 4b. Yksittäisen käyttäjän tekemättömien/tehtyjen muistutusten listaaminen

Jos viimeisellä rivillä on _FALSE_, haetaan tekemättömät muistutukset. Jos viimeisellä tivillä on _TRUE_, haetaan tehdyt muistutukset. Edelliseen kyselyyn verrattuna käyttäjän tietojen liittäminen ei ole tarpeellista, sillä sovelluksessa relevantin käyttäjän _account_id_ tiedetään _current_user_-muuttujan avulla.

```
SELECT Reminder.id, Reminder.note, Reminder.date_remind, Reminder.done, Contract.id, Contract.name FROM Reminder
    JOIN Contract ON Reminder.contract_id = Contract.id
    WHERE Reminder.account_id = :account_id AND Reminder.done = FALSE/TRUE;
```

### 4c. Käyttäjän sellaisten tekemättömien muistutusten listaaminen, joiden päivämäärä on täynnä

Tämän toiminnon avulla kirjautuneen käyttäjän etusivulle tuodaan sellaiset muistutukset, joiden päivämäärä on täynnä ja joita ei vielä ole merkitty tekemättömäksi. Kyselylle annetaan syötteinä käyttäjän _account_id_ sekä nykyinen päivämäärä (_date.today()_).

```
SELECT Reminder.id, Reminder.note, Reminder.date_remind, Reminder.done, Contract.id, Contract.name FROM Reminder
    JOIN Contract ON Reminder.contract_id = Contract.id
    WHERE Reminder.account_id = ? AND Reminder.done = FALSE AND Reminder.date_remind <= ?
    ORDER BY Reminder.date_remind ASC;
```

### 4d. Muistutuksen lisääminen kaikille käyttäjille, joiden sopimuksiin liitetty osapuoli on asetettu konkurssiin

Kun osapuoli asetetaan konkurssiin, sovellus lisää muistutuksen kaikille niille käyttäjille, joiden sopimuksiin kyseinen osapuoli on liitetty. Käytännössä _create_bankruptcy_reminders_ saa syötteenä kyseisen osapuolen tiedot mukaan lukien sen sopimuslistan. Syötettäviä rivejä tulee siis niin monta kuin kyseisen osapuolen sopimuslistassa on sopimuksia.

```
INSERT INTO Reminder
    (note, date_remind, done, contract_id, account_id)
    VALUES
    (?, ?, FALSE, ?, ?),
    (?, ?, FALSE, ?, ?),
    (?, ?, FALSE, ?, ?);
```

## 5. Käyttäjät

### 5a. Sopimusten määrän liittäminen käyttäjälistaukseen

Tätä kyselyä käytetään käyttäjälistaukessa, jossa näytetään kunkin käyttäjän tietojen lisäksi kunkin käyttäjän omistamien sopimusten määrä.

```
SELECT Account.id, Account.username, Account.name, COUNT(Contract.id) FROM Account
    LEFT JOIN Contract ON Contract.account_id = Account.id
    GROUP BY Account.id;
```
