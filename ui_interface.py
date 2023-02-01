# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomSlideMenu
from Custom_Widgets.Widgets import QCustomStackedWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1231, 738)
        MainWindow.setStyleSheet(u"* {\n"
"	/*background-color: rgb(207, 242, 255);*/\n"
"	background-color: rgb(155, 207, 212);\n"
"	border: None;\n"
"	font-size: 9pt;\n"
"}\n"
"\n"
"QPushButton {\n"
"	border-radius: 10px;\n"
"	padding-top: 4px;\n"
"	padding-bottom: 4px;\n"
"}\n"
"\n"
"QComboBox:focus{\n"
"	border: 2px solid black;\n"
"}\n"
"\n"
"QComboBox{\n"
"	height: 20px;\n"
"	border-radius: 14px;\n"
"	background-color: rgb(100, 207, 212);\n"
"	border: 2px solid rgb(100, 207, 212);\n"
"	padding: 2px 10px;\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down{\n"
"	border: None;\n"
"}\n"
"\n"
"QComboBox::down-arrow{\n"
"	width: 20px;\n"
"	margin-right: 20px;\n"
"}\n"
"\n"
"#frame_2 {\n"
"	border: 2px solid black;\n"
"	padding: 7px;\n"
"	border-radius: 15px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.LeftMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.LeftMenuContainer.setObjectName(u"LeftMenuContainer")
        self.LeftMenuContainer.setMinimumSize(QSize(140, 0))
        self.LeftMenuContainer.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid black;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.LeftMenuContainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.LeftMenuContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(11, 20, 0, -1)
        self.generate_btn = QPushButton(self.frame)
        self.generate_btn.setObjectName(u"generate_btn")
        self.generate_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.generate_btn)

        self.add_btn = QPushButton(self.frame)
        self.add_btn.setObjectName(u"add_btn")
        self.add_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.add_btn)

        self.delete_btn = QPushButton(self.frame)
        self.delete_btn.setObjectName(u"delete_btn")
        self.delete_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.delete_btn)


        self.verticalLayout_2.addWidget(self.frame)

        self.verticalSpacer = QSpacerItem(20, 560, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.LeftMenuContainer)

        self.mainBodyContainer = QWidget(self.centralwidget)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy)
        self.mainBodyContainer.setStyleSheet(u"")
        self.verticalLayout_6 = QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.mainBodyContent = QWidget(self.mainBodyContainer)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy1)
        self.horizontalLayout_5 = QHBoxLayout(self.mainBodyContent)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(10, 0, 10, 0)
        self.mainPages = QCustomStackedWidget(self.mainBodyContent)
        self.mainPages.setObjectName(u"mainPages")
        self.mainPages.setStyleSheet(u"")
        self.page_generation = QWidget()
        self.page_generation.setObjectName(u"page_generation")
        self.verticalLayout_3 = QVBoxLayout(self.page_generation)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_2 = QFrame(self.page_generation)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(100)
        self.gridLayout.setVerticalSpacing(20)
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 20))
        self.label.setMaximumSize(QSize(16777215, 20))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.auteurs_list = QComboBox(self.frame_2)
        self.auteurs_list.setObjectName(u"auteurs_list")

        self.gridLayout.addWidget(self.auteurs_list, 1, 0, 1, 1)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 30))
        self.label_3.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.difficultes_list = QComboBox(self.frame_2)
        self.difficultes_list.addItem("")
        self.difficultes_list.addItem("")
        self.difficultes_list.addItem("")
        self.difficultes_list.addItem("")
        self.difficultes_list.setObjectName(u"difficultes_list")

        self.gridLayout.addWidget(self.difficultes_list, 3, 0, 1, 1)

        self.keywors_list = QComboBox(self.frame_2)
        self.keywors_list.setObjectName(u"keywors_list")

        self.gridLayout.addWidget(self.keywors_list, 1, 1, 1, 1)

        self.corrige_checkbox = QCheckBox(self.frame_2)
        self.corrige_checkbox.setObjectName(u"corrige_checkbox")

        self.gridLayout.addWidget(self.corrige_checkbox, 3, 1, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.frame_4 = QFrame(self.page_generation)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setSpacing(40)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.table = QTableWidget(self.frame_4)
        if (self.table.columnCount() < 7):
            self.table.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.table.setObjectName(u"table")
        self.table.setStyleSheet(u"background-color: rgb(255, 211, 212);")

        self.horizontalLayout_4.addWidget(self.table)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.page_generation)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid black;\n"
"	height: 22px;\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setSpacing(90)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(50, 10, 50, 5)
        self.ajouter = QPushButton(self.frame_3)
        self.ajouter.setObjectName(u"ajouter")

        self.horizontalLayout_6.addWidget(self.ajouter)

        self.clean_btn = QPushButton(self.frame_3)
        self.clean_btn.setObjectName(u"clean_btn")
        self.clean_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_6.addWidget(self.clean_btn)

        self.creation_btn = QPushButton(self.frame_3)
        self.creation_btn.setObjectName(u"creation_btn")
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.creation_btn.setFont(font)
        self.creation_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_6.addWidget(self.creation_btn)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.mainPages.addWidget(self.page_generation)
        self.add_page = QWidget()
        self.add_page.setObjectName(u"add_page")
        self.listWidget = QListWidget(self.add_page)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(60, 40, 391, 561))
        self.listWidget.setStyleSheet(u"background-color: rgb(255, 170, 0);")
        self.mainPages.addWidget(self.add_page)
        self.delete_page = QWidget()
        self.delete_page.setObjectName(u"delete_page")
        self.mainPages.addWidget(self.delete_page)

        self.horizontalLayout_5.addWidget(self.mainPages)


        self.verticalLayout_6.addWidget(self.mainBodyContent)


        self.horizontalLayout.addWidget(self.mainBodyContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.mainPages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.generate_btn.setText(QCoreApplication.translate("MainWindow", u"G\u00e9n\u00e9rer", None))
        self.add_btn.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.delete_btn.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Mot Cl\u00e9 :", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Auteur :", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Difficult\u00e9 :", None))
        self.difficultes_list.setItemText(0, "")
        self.difficultes_list.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.difficultes_list.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.difficultes_list.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))

        self.corrige_checkbox.setText(QCoreApplication.translate("MainWindow", u"Corrig\u00e9", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"R\u00e9f exo", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Fichier", None));
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Auteur", None));
        ___qtablewidgetitem3 = self.table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Difficult\u00e9", None));
        ___qtablewidgetitem4 = self.table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Mot Cl\u00e9s", None));
        ___qtablewidgetitem5 = self.table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Corrig\u00e9", None));
        ___qtablewidgetitem6 = self.table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Auteur Corrig\u00e9", None));
        self.ajouter.setText(QCoreApplication.translate("MainWindow", u"Ajouter des exercices", None))
        self.clean_btn.setText(QCoreApplication.translate("MainWindow", u"Nettoyer la table", None))
        self.creation_btn.setText(QCoreApplication.translate("MainWindow", u"Cr\u00e9er le fichier", None))
    # retranslateUi

