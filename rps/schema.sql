DROP TABLE IF EXISTS game;

CREATE TABLE game (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	joincode TEXT UNIQUE,
	name1 TEXT,
	move1 INTEGER,
	name2 TEXT,
	move2 INTEGER
);
