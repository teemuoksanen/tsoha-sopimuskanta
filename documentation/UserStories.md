# Käyttäjätarinat

Käyttäjätarinoiden (_user story_) perässä oleva numero viittaa dokumentin lopussa oleviin SQL-kyselyihin.

## Käyttäjänä voin...
- ...listata kaikki sopimukset sekä osapuolet. _(1d)_
- ...lisätä uusia sopimuksia (jolloin minut merkitään sopimuksen omistajaksi), osapuolia sekä sopimuksiin liittyviä muistutuksia. _(1a)_
- ...muokata omistamieni sopimusten tietoja tai poistaa kyseiset sopimukset. _(1b, 1c)_
- ...muokata tai poistaa omia muistutuksiani. _(1b, 1c)_
- ...muokata kaikkien osapuolten tietoja. _(1b)_
- ...muokata omia tietojani ja vaihtaa salasanaani. _(1b)_
- ...lisätä osapuolia niihin sopimuksiin, joiden omistaja olen. _(2b)_

## Ylläpitäjänä voin lisäksi...
- ...luoda uusia käyttäjiä. _(1a)_
- ...poistaa minkä tahansa sopimuksen, osapuolen (jos osapuoli ei ole aktiivisena jollain sopimuksella), muistutuksen tai käyttäjän. _(1c)_
- ...muokata mitä tahansa sopimusta, muistutusta tai käyttäjää. _(1b)_
- ...lisätä muistutuksia kaikille käyttäjille. _(1a)_

## Yleisiä käyttötapauksia
- Jos sopimukselle lisätään päättymispäivä, sopimuksen omistajalle lisätään muistutus. _(1a)_
- Jos osapuoli asetetaan konkurssiin, kaikille osapuolten sopimusten omistajille lisätään muistutus. _(1a)_

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
    (SELECT party_id FROM ContractParty WHERE contract_id IS ?)
    GROUP BY Party.id;
```

### 2b. Osapuolen lisääminen sopimukselle

Osapuoli lisätään sopimukselle liitostaulun avulla. Liitostalussa _contract_id_ viittaa sopimuksen id-numeroon ja _party_id_ osapuolen id-numeroon.

```
INSERT INTO ContractParty
    (contract_id, party_id)
    VALUES (?, ?);
```

## 3. Osapuolet

_osio kesken_

## 4. Muistutukset

_osio kesken_

## 5. Käyttäjät

### 5a. Sopimusten määrän liittäminen käyttäjälistaukseen

Tätä kyselyä käytetään käyttäjälistaukessa, jossa näytetään kunkin käyttäjän tietojen lisäksi kunkin käyttäjän omistamien sopimusten määrä.

```
SELECT Account.id, Account.username, Account.name, COUNT(Contract.id) FROM Account
    LEFT JOIN Contract ON Contract.account_id = Account.id
    GROUP BY Account.id;
```
