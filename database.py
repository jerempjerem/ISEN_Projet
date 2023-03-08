import sqlite3


class Database():

    GET_ALL_EXERCICES = """
        SELECT 
            ExercicesId,
            Ref_exo, 
            EXERCICES.Fichier, 
            AUTEURS.Nom,
            Difficulte,
            CORRIGES.Fichier,
            AUTEURS_CORRIGES.Nom
        FROM EXERCICES
        LEFT JOIN CORRIGES ON EXERCICES.CorrigeID_ext = CORRIGES.CorrigeID
        INNER JOIN AUTEURS ON EXERCICES.AuteurID_ext = AUTEURS.AuteurID
        LEFT JOIN AUTEURS AS AUTEURS_CORRIGES ON CORRIGES.AuteurID_ext = AUTEURS_CORRIGES.AuteurID
    """

    GET_ALL_KEYWORD = """
        SELECT Keyword
        FROM EXERCICES
        INNER JOIN Keywords_Liaisons ON EXERCICES.ExercicesID = Keywords_Liaisons.ExerciceId_ext
        INNER JOIN KEYWORDS ON KEYWORDS.KeywordID = Keywords_Liaisons.KeywordId_ext
        WHERE EXERCICES.Fichier = "exo2.tex"
    """

    def __init__(self, database_path: str):
        self.database_path = database_path

    def fetch(self, query: str) -> list:
        """
        Fonction permettant de récupérer des données dans une database donnée.

        :param query: requête SQL que l'on veut exécuter
        :return: renvoie les données récupérées grâce à cette requête
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

        :param query: requête SQL que l'on veut exécuter
        """ 
        if self.connect():
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            cursor.close()

    def connect(self) -> bool:
        """
        Fonction permettant de se connecter à la database donnée.

        :return: renvoie un booléen True si nous sommes connecté, False sinon
        """ 

        try:
            self.connection = sqlite3.connect(self.database_path)
            return True
        except Exception as e:
            self.connection = None
            print(f'Erreur lors de la connexion a la base de donnée: {e}')
            return False
