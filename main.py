# pyside2-uic interface.ui -o ui_interface.py
# pdflatex -interaction=batchmode -no-file-line-error -halt-on-error test.tex
# https://miktex.org/download pdflatex et installer package currfile

from database import Database
from ui_interface import *
import sys
import os

DATABASE_PATH = 'db/database_test.db'
database = Database(database_path=DATABASE_PATH)

def fusionner_fichier_tex(fichiers_path: list, nom_du_fichier_final: str):
    final_tex = ""
    for index, fichier in enumerate(fichiers_path):
        with open(fichier, 'r') as tex_file:
            content = tex_file.read()
            if index == 0:
                content = content.replace('\end{document}', '')
            else:
                content = content.replace('\documentclass{article}', '')
                content = content.replace(r'\begin{document}', '')
                content = content.replace('\end{document}', '')
            final_tex += content
    final_tex += '\end{document}'

    with open(f'{nom_du_fichier_final}.tex', 'w') as final_tex_file:
        final_tex_file.write(final_tex)

def tex_to_pdf(file_name: str):
    os.system(f'pdflatex -interaction=batchmode -no-file-line-error -halt-on-error {file_name}.tex')
    os.remove(f"{file_name}.aux")
    os.remove(f"{file_name}.log")


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        # Initialization GUI
        self.load_auteurs()
        self.load_keywords()

        self.ui.table.verticalHeader().setVisible(False)
        [self.ui.table.horizontalHeader().setSectionResizeMode(i, QHeaderView.Stretch) for i in range(6)]

        self.ui.ajouter.clicked.connect(self.fetch_exercices)
        self.ui.clean_btn.clicked.connect(self.clean)
        self.ui.creation_btn.clicked.connect(self.generate)

        # Autres Variables
        self.loaded_exercices = []

    def fetch_exercices(self):
        auteur = f'"{self.ui.auteurs_list.currentText()}"' if self.ui.auteurs_list.currentText() != "" else "AUTEURS.Nom"
        difficulte = f'"{self.ui.difficultes_list.currentText()}"' if self.ui.difficultes_list.currentText() != ""else "Difficulte"
        keyword = f'"{self.ui.keywors_list.currentText()}"' if self.ui.keywors_list.currentText() != "" else "KEYWORDS.Keyword"

        condition = f"WHERE AUTEURS.Nom = {auteur} AND Difficulte = {difficulte} AND KEYWORDS.Keyword = {keyword}"

        result = database.fetch(database.GET_ALL_EXERCICES + condition)
        [self.load_exercice(exercice) for exercice in result]

    def load_auteurs(self):
        self.ui.auteurs_list.clear()
        self.ui.auteurs_list.addItems(self._get_auteurs())

    def load_keywords(self):
        self.ui.keywors_list.clear()
        self.ui.keywors_list.addItems(self._get_keyword())

    def load_exercice(self, exercice: list):
        if exercice in self.loaded_exercices:
            return
        
        row = self.ui.table.rowCount()
        self.ui.table.insertRow(row)
        self.loaded_exercices.append(exercice)

        ref = exercice[0] if not exercice[1] else exercice[1]
        ref_exo = QTableWidgetItem(str(ref))
        ref_exo.setFlags(Qt.NoItemFlags)

        fichier = QTableWidgetItem(str(exercice[2]))
        fichier.setFlags(Qt.NoItemFlags)

        auteur = QTableWidgetItem(str(exercice[3]))
        auteur.setFlags(Qt.NoItemFlags)

        difficulte = QTableWidgetItem(str(exercice[4]))
        difficulte.setFlags(Qt.NoItemFlags)

        keywords = QTableWidgetItem(str(exercice[5]))
        keywords.setFlags(Qt.NoItemFlags)

        corrige = QTableWidgetItem(str(exercice[6]))
        corrige.setFlags(Qt.NoItemFlags)

        auteur_corrige = QTableWidgetItem(str(exercice[7]))
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

    def generate(self):
        if len(self.loaded_exercices) == 0:
            return

        corrige = True if self.ui.corrige_checkbox.isChecked() else False
        files = []
        for exercice in self.loaded_exercices:
            files.append(f"exercices/{exercice[2]}")
            if corrige:
                files.append(f"exercices/{exercice[6]}")
        
        print(files)
        final_name = 'TD_Final'
        fusionner_fichier_tex(files, final_name) 
        tex_to_pdf(final_name)

    def clean(self):
        self.loaded_exercices = []
        self.ui.table.setRowCount(0)

    def _get_auteurs(self):
        return [''] + [a[0] for a in database.fetch("SELECT Nom FROM AUTEURS")]

    def _get_keyword(self):
        return [''] + [k[0] for k in database.fetch("SELECT Keyword FROM KEYWORDS")]


app = QApplication(sys.argv)
window = MainWindow()
window.show()

sys.exit(app.exec_())


