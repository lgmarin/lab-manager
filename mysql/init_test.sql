CREATE SCHEMA IF NOT EXISTS `lab_manager` ;
USE `AccountOwner` ;

CREATE TABLE comment (
	id INTEGER NOT NULL, 
	text TEXT NOT NULL, 
	date_created DATETIME, 
	author INTEGER NOT NULL, 
	post_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(author) REFERENCES user (id) ON DELETE CASCADE, 
	FOREIGN KEY(post_id) REFERENCES post (id) ON DELETE CASCADE
)

CREATE TABLE post (
	id INTEGER NOT NULL, 
	text TEXT NOT NULL, 
	date_created DATETIME, 
	author INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(author) REFERENCES user (id) ON DELETE CASCADE
)

CREATE TABLE project (
	id INTEGER NOT NULL, 
	name VARCHAR(150), 
	date_created DATETIME, 
	active BOOLEAN NOT NULL, 
	created_by INTEGER, 
	PRIMARY KEY (id), 
	UNIQUE (name), 
	FOREIGN KEY(created_by) REFERENCES user (id)
)

CREATE TABLE user (
	id INTEGER NOT NULL, 
	email VARCHAR(50), 
	name VARCHAR(150), 
	password VARCHAR(128), 
	date_created DATETIME, 
	biometry BOOLEAN NOT NULL, 
	project INTEGER NOT NULL, 
	grr INTEGER, 
	course VARCHAR(50), 
	approved_by INTEGER, 
	date_approved DATETIME, 
	approved BOOLEAN NOT NULL, 
	admin BOOLEAN NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (email), 
	UNIQUE (grr)
)