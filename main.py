from database import Database

databse_path = 'db/database_test.db'

database = Database(database_path=databse_path)

# 'INSERT INTO AUTEURS VALUES (NULL, "Luquet")'
# 'INSERT INTO CORRIGES VALUES (NULL, "exo1.tex", 1)'
# 'INSERT INTO KEYWORDS VALUES (NULL, "Calculs")'
# 'INSERT INTO EXERCICES VALUES (NULL, "exo1.tex", NULL, 1, 2, 1, 4)'

AUTEURS = [a[0] for a in database.fetch("SELECT Nom FROM AUTEURS")]
KEYWORDS = [k[0] for k in database.fetch("SELECT Keyword FROM KEYWORDS")]
print(AUTEURS)
print(KEYWORDS)

query = f"""
    SELECT 
        Ref_exo AS "Réf exo", 
        EXERCICES.Fichier AS "Fichier", 
        AUTEURS.Nom AS "Auteur",
        Difficulte AS "Difficulté",
        KEYWORDS.Keyword AS "Mot Clé", 
        CORRIGES.Fichier AS "Corrigé",
        AUTEURS_CORRIGES.Nom AS "Auteur Corrigé"
    FROM EXERCICES
    LEFT JOIN CORRIGES ON EXERCICES.CorrigeID_ext = CORRIGES.CorrigeID
    INNER JOIN AUTEURS ON EXERCICES.AuteurID_ext = AUTEURS.AuteurID
    INNER JOIN KEYWORDS ON EXERCICES.KeywordID_ext = KEYWORDS.KeywordID
    LEFT JOIN AUTEURS AS AUTEURS_CORRIGES ON CORRIGES.AuteurID_ext = AUTEURS_CORRIGES.AuteurID
    WHERE AUTEURS.Nom = '{AUTEURS[0]}'
"""
reslt = database.fetch(query)
print(reslt)


