# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mp3.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_FormUno(object):
    def setupUi(self, FormUno):
        if not FormUno.objectName():
            FormUno.setObjectName(u"FormUno")
        FormUno.resize(400, 250)
        icon = QIcon()
        icon.addFile(u"../Downloads/icons8-carpeta-de-pel\u00edculas-96.png", QSize(), QIcon.Normal, QIcon.Off)
        FormUno.setWindowIcon(icon)
        FormUno.setStyleSheet(u"QObject{\n"
"	background-color: #555;\n"
"}")
        self.label_titulo_mp3 = QLabel(FormUno)
        self.label_titulo_mp3.setObjectName(u"label_titulo_mp3")
        self.label_titulo_mp3.setGeometry(QRect(80, 10, 221, 31))
        self.label_titulo_mp3.setStyleSheet(u"font: 87 14pt \"Arial Black\";\n"
"color: white;\n"
"background-color: #ccc;\n"
"border: 2px solid #555;")
        self.txt_link_mp3 = QLineEdit(FormUno)
        self.txt_link_mp3.setObjectName(u"txt_link_mp3")
        self.txt_link_mp3.setGeometry(QRect(70, 120, 261, 20))
        self.txt_link_mp3.setStyleSheet(u"background-color: white;")
        self.label_link = QLabel(FormUno)
        self.label_link.setObjectName(u"label_link")
        self.label_link.setGeometry(QRect(70, 100, 261, 16))
        self.label_link.setStyleSheet(u"font: 75 10pt \"Arial\";\n"
"color: white;")
        self.pushButton_mp3 = QPushButton(FormUno)
        self.pushButton_mp3.setObjectName(u"pushButton_mp3")
        self.pushButton_mp3.setGeometry(QRect(160, 160, 81, 31))
        self.pushButton_mp3.setStyleSheet(u"font: 87 8pt \"Arial Black\";\n"
"color: white;")
        self.pushButton_back = QPushButton(FormUno)
        self.pushButton_back.setObjectName(u"pushButton_back")
        self.pushButton_back.setGeometry(QRect(0, 0, 61, 21))
        self.pushButton_back.setStyleSheet(u"color: white;\n"
"font: 87 10pt \"Arial Black\";")
        self.label = QLabel(FormUno)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 200, 261, 41))
        self.label.setStyleSheet(u"font: 87 14pt \"Arial Black\";\n"
"color: white;\n"
"border: 2px solid #555;")

        self.retranslateUi(FormUno)

        QMetaObject.connectSlotsByName(FormUno)
    # setupUi

    def retranslateUi(self, FormUno):
        FormUno.setWindowTitle(QCoreApplication.translate("FormUno", u"MP3", None))
        self.label_titulo_mp3.setText(QCoreApplication.translate("FormUno", u"Descarga MP3", None))
        self.label_link.setText(QCoreApplication.translate("FormUno", u"Inserta el Link de click y espere el mensaje:", None))
        self.pushButton_mp3.setText(QCoreApplication.translate("FormUno", u"Descargar", None))
        self.pushButton_back.setText(QCoreApplication.translate("FormUno", u"Menu", None))
        self.label.setText("")
    # retranslateUi

