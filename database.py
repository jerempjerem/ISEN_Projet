import sqlite3


# Piste de reflexion pour adapter la database a plusieurs keywords
#
# 
#
#
#


class Database():

    GET_ALL_EXERCICES = """
        SELECT 
            Ref_exo, 
            EXERCICES.Fichier, 
            AUTEURS.Nom,
            Difficulte,
            KEYWORDS.Keyword, 
            CORRIGES.Fichier,
            AUTEURS_CORRIGES.Nom
        FROM EXERCICES
        LEFT JOIN CORRIGES ON EXERCICES.CorrigeID_ext = CORRIGES.CorrigeID
        INNER JOIN AUTEURS ON EXERCICES.AuteurID_ext = AUTEURS.AuteurID
        INNER JOIN KEYWORDS ON EXERCICES.KeywordID_ext = KEYWORDS.KeywordID
        LEFT JOIN AUTEURS AS AUTEURS_CORRIGES ON CORRIGES.AuteurID_ext = AUTEURS_CORRIGES.AuteurID
    """

    def __init__(self, database_path: str):
        self.database_path = database_path

    def fetch(self, query: str) -> list:
        """
            Fonction permettant de récupérer des données dans une database donnée.

            Cette fonction prend en argument une requête SQL que l'on veut exécuter, 
            et renvoie les données récupérées grâce à cette requête.       
        """
        if self.connect():
            cursor = self.connection.cursor()
            response = cursor.execute(query)
            data = response.fetchall()
            cursor.close()
            return data
        
        return []
        
    def edit(self, query: str):
        """
            Fonction permettant de modifier une database donnée (INSERT, DELETE, CHANGE).

            Cette fonction prend en argument une requête SQL que l'on veut exécuter, 
            et ne renvoie rien.   
        """
        if self.connect():
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            cursor.close()

    def connect(self) -> bool:
        """
            Fonction permettant de se connecter à la database donnée.

            Cette fonction ne prend pas d'arguments et renvoie un booléen
        """
        try:
            self.connection = sqlite3.connect(self.database_path)
            return True
        except Exception as e:
            self.connection = None
            print(f'Erreur lors de la connexion a la base de donnée: {e}')
            return False