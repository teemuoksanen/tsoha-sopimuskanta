# Käyttäjätarinat

Käyttäjätarinoiden (_user story_) perässä oleva numero viittaa dokumentin lopussa oleviin SQL-kyselyihin.

## Käyttäjänä voin...
- ...listata kaikki sopimukset sekä osapuolet. (1)
- ...lisätä uusia sopimuksia (jolloin minut merkitään sopimuksen omistajaksi), osapuolia sekä sopimuksiin liittyviä muistutuksia. (2)
- ...muokata omistamieni sopimusten tietoja tai poistaa kyseiset sopimukset. (3)
- ...muokata tai poistaa omia muistutuksiani. (4)
- ...muokata kaikkien osapuolten tietoja. (5)
- ...muokata omia tietojani ja vaihtaa salasanaani.
- ...lisätä osapuolia niihin sopimuksiin, joiden omistaja olen. (4)

## Ylläpitäjänä voin lisäksi...
- ...luoda uusia käyttäjiä.
- ...poistaa minkä tahansa sopimuksen, osapuolen (jos osapuoli ei ole aktiivisena jollain sopimuksella), muistutuksen tai käyttäjän.
- ...muokata mitä tahansa sopimusta, muistutusta tai käyttäjää.
- ...lisätä muistutuksia kaikille käyttäjille.

## Yleisiä käyttötapauksia
- Jos sopimukselle lisätään päättymispäivä, sopimuksen omistajalle lisätään muistutus.
- Jos osapuoli asetetaan konkurssiin, kaikille osapuolten sopimusten omistajille lisätään muistutus.

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

### 1c. Kaikkien kohteiden listaaminen

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

## 3. Osapuolet

_osio kesken_

## 4. Muistutukset

_osio kesken_

## 5. Käyttäjät

### 4a. Sopimusten määrän liittäminen käyttäjälistaukseen

Tätä kyselyä käytetään käyttäjälistaukessa, jossa näytetään kunkin käyttäjän tietojen lisäksi kunkin käyttäjän omistamien sopimusten määrä.

```
SELECT Account.id, Account.username, Account.name, COUNT(Contract.id) FROM Account
    LEFT JOIN Contract ON Contract.account_id = Account.id
    GROUP BY Account.id;
```
