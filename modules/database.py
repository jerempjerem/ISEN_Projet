import sqlite3

class Database():
    def __init__(self, database_path: str):
        self.database_path = database_path

    def fetch(self, query: str):
        """
            fonction qui permet de recuperer des données dans la database
            et qui prend en entrée la requete que l'on souhaite faire
        """
        if not self.connection:
            print('Aucune connexion existante')
            return None

        cursor = self.connection.cursor()
        response = cursor.execute(query)
        data = response.fetchall()
        cursor.close()
        return data

    def edit(self, query: str):
        """
            fonction qui permet d'ajouter, de supprimer, ou de modifier une donnée dans la database
            et qui prend en entrée la requete que l'on souhaite faire
        """
        if not self.connection:
            print('Aucune connexion existante')
            return None

        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        cursor.close()
        return

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.database_path)
        except Exception as e:
            self.connection = None
            print(f'Erreur lors de la connexion a la base de donnée: {e}')