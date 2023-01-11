# pyside2-uic interface.ui -o ui_interface.py

from database import Database
import sys

DATABASE_PATH = 'db/database_test.db'

database = Database(database_path=DATABASE_PATH)

# 'INSERT INTO AUTEURS VALUES (NULL, "Luquet")'
# 'INSERT INTO CORRIGES VALUES (NULL, "exo1.tex", 1)'
# 'INSERT INTO KEYWORDS VALUES (NULL, "Calculs")'
# 'INSERT INTO EXERCICES VALUES (NULL, "exo1.tex", NULL, 1, 2, 1, 4)'

AUTEURS = [''] + [a[0] for a in database.fetch("SELECT Nom FROM AUTEURS")]
KEYWORDS = [''] + [k[0] for k in database.fetch("SELECT Keyword FROM KEYWORDS")]
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


########################################################################
from ui_interface import *
from PySide2 import QtWidgets
########################################################################

########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        ########################################################################
        
        self.load_auteurs()
        self.load_keywords()
        self.ui.table.verticalHeader().setVisible(False)
        [self.ui.table.horizontalHeader().setSectionResizeMode(i, QHeaderView.Stretch) for i in range(6)]

        self.ui.ajouter.clicked.connect(self.fetch_exercices)
        self.corrige = False

    def fetch_exercices(self):
        auteur = self.ui.auteurs_list.currentText() if self.ui.auteurs_list.currentText() != "" else None
        difficulte = self.ui.difficultes_list.currentText() if self.ui.difficultes_list.currentText() != "" else None
        keyword = self.ui.keywors_list.currentText() if self.ui.keywors_list.currentText() != "" else None
        self.corrige = True if self.ui.corrige_checkbox.isChecked() else False

        if auteur or difficulte or keyword:
            condition = "WHERE "
            if auteur:
                condition += f'AUTEURS.Nom = "{auteur}" '
            if difficulte:
                condition += f'AND Difficulte = {difficulte} '
            if keyword:
                condition += f'AND KEYWORDS.Keyword = "{keyword}"'
        else:
            condition = ""

        result = database.fetch(database.GET_ALL_EXERCICES + condition)
        [self.load_exercice(exercice) for exercice in result]


    def load_auteurs(self):
        self.ui.auteurs_list.clear()
        self.ui.auteurs_list.addItems(AUTEURS)

    def load_keywords(self):
        self.ui.keywors_list.clear()
        self.ui.keywors_list.addItems(KEYWORDS)

    def load_exercice(self, exercice: list):
        row = self.ui.table.rowCount()
        self.ui.table.insertRow(row)

        ref_exo = QTableWidgetItem(str(exercice[0]))
        ref_exo.setFlags(Qt.NoItemFlags)

        fichier = QTableWidgetItem(str(exercice[1]))
        fichier.setFlags(Qt.NoItemFlags)

        auteur = QTableWidgetItem(str(exercice[2]))
        auteur.setFlags(Qt.NoItemFlags)

        difficulte = QTableWidgetItem(str(exercice[3]))
        difficulte.setFlags(Qt.NoItemFlags)

        keywords = QTableWidgetItem(str(exercice[4]))
        keywords.setFlags(Qt.NoItemFlags)

        corrige = QTableWidgetItem(str(exercice[5]))
        corrige.setFlags(Qt.NoItemFlags)

        auteur_corrige = QTableWidgetItem(str(exercice[6]))
        auteur_corrige.setFlags(Qt.NoItemFlags)

        self.ui.table.setItem(row, 0, ref_exo)
        self.ui.table.setItem(row, 1, fichier)
        self.ui.table.setItem(row, 2, auteur)
        self.ui.table.setItem(row, 3, difficulte)
        self.ui.table.setItem(row, 4, keywords)
        self.ui.table.setItem(row, 5, corrige)
        self.ui.table.setItem(row, 6, auteur_corrige)

        self.ui.table.item(row, 0).setTextAlignment(Qt.AlignCenter)
        self.ui.table.item(row, 1).setTextAlignment(Qt.AlignCenter)
        self.ui.table.item(row, 2).setTextAlignment(Qt.AlignCenter)
        self.ui.table.item(row, 3).setTextAlignment(Qt.AlignCenter)
        self.ui.table.item(row, 4).setTextAlignment(Qt.AlignCenter)
        self.ui.table.item(row, 5).setTextAlignment(Qt.AlignCenter)
        self.ui.table.item(row, 6).setTextAlignment(Qt.AlignCenter)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

sys.exit(app.exec_())


