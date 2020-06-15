# Tietokannan tekstimuotoinen kuvaus

## Party (osapuolet)

```
CREATE TABLE party (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	business_id VARCHAR(9), 
	address_street VARCHAR(144), 
	address_postalcode VARCHAR(5), 
	address_city VARCHAR(50), 
	bankrupt BOOLEAN NOT NULL, 
	PRIMARY KEY (id), 
	CHECK (bankrupt IN (0, 1))
);
```

## Contract (sopimukset)

```
CREATE TABLE contract (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	date_signed DATE, 
	date_entry DATE, 
	date_expiry DATE, 
	account_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id)
);
```

## Reminder (muistutukset)

```
CREATE TABLE reminder (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	note VARCHAR(250) NOT NULL, 
	date_remind DATE, 
	done BOOLEAN NOT NULL, 
	contract_id INTEGER NOT NULL, 
	account_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	CHECK (done IN (0, 1)), 
	FOREIGN KEY(contract_id) REFERENCES contract (id), 
	FOREIGN KEY(account_id) REFERENCES account (id)
);
```

## Account (käyttäjät)

```
CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	user_role VARCHAR(80) NOT NULL, 
	PRIMARY KEY (id)
);
```

## ContractParty (sopimusten ja osapuolten liitostaulu)

```
CREATE TABLE IF NOT EXISTS "ContractParty" (
	contract_id INTEGER NOT NULL, 
	party_id INTEGER NOT NULL, 
	PRIMARY KEY (contract_id, party_id), 
	FOREIGN KEY(contract_id) REFERENCES contract (id), 
	FOREIGN KEY(party_id) REFERENCES party (id)
);
```