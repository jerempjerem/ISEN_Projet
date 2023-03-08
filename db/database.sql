-- Creation de la table des AUTEURS
CREATE TABLE "AUTEURS" (
	"AuteurID"	INTEGER,
	"Nom"	TEXT NOT NULL,
	PRIMARY KEY("AuteurID" AUTOINCREMENT)
);

-- Creation de la table des CORRIGES
CREATE TABLE "CORRIGES" (
	"CorrigeID"	INTEGER,
	"Fichier"	TEXT NOT NULL,
	"AuteurID_ext"	INTEGER NOT NULL,
	PRIMARY KEY("CorrigeID" AUTOINCREMENT)
);

-- Creation de la table des KEYWORDS
CREATE TABLE "KEYWORDS" (
	"KeywordID"	INTEGER,
	"Keyword"	TEXT NOT NULL,
	PRIMARY KEY("KeywordID" AUTOINCREMENT)
);

-- Creation de la table des EXERCICES
CREATE TABLE "EXERCICES" (
	"ExercicesID"	INTEGER,
	"Fichier"	TEXT NOT NULL,
	"Ref_exo"	TEXT,
	"Difficulte"	TEXT NOT NULL,
	"AuteurID_ext"	INTEGER NOT NULL,
	"CorrigeID_ext"	INTEGER
	PRIMARY KEY("ExercicesID" AUTOINCREMENT)
);

CREATE TABLE "Keywords_Liaisons" (
	"LiaisonId"	INTEGER,
	"ExerciceId_ext"	INTEGER NOT NULL,
	"KeywordId_ext"	INTEGER NOT NULL,
	PRIMARY KEY("LiaisonId" AUTOINCREMENT)
);