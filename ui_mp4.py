# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mp4.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_FormDos(object):
    def setupUi(self, FormDos):
        if not FormDos.objectName():
            FormDos.setObjectName(u"FormDos")
        FormDos.resize(400, 250)
        icon = QIcon()
        icon.addFile(u"../Downloads/icons8-carpeta-de-pel\u00edculas-96.png", QSize(), QIcon.Normal, QIcon.Off)
        FormDos.setWindowIcon(icon)
        FormDos.setStyleSheet(u"QObject{\n"
"	background-color: #555;\n"
"}")
        self.label_titulo_mp4 = QLabel(FormDos)
        self.label_titulo_mp4.setObjectName(u"label_titulo_mp4")
        self.label_titulo_mp4.setGeometry(QRect(80, 10, 221, 31))
        self.label_titulo_mp4.setStyleSheet(u"font: 87 14pt \"Arial Black\";\n"
"color: white;\n"
"background-color: #ccc;\n"
"border: 2px solid #555;")
        self.label_link_mp4 = QLabel(FormDos)
        self.label_link_mp4.setObjectName(u"label_link_mp4")
        self.label_link_mp4.setGeometry(QRect(60, 90, 271, 20))
        self.label_link_mp4.setStyleSheet(u"font: 87 10pt \"Arial\";\n"
"color: white;")
        self.txt_link_mp4 = QLineEdit(FormDos)
        self.txt_link_mp4.setObjectName(u"txt_link_mp4")
        self.txt_link_mp4.setGeometry(QRect(60, 120, 271, 20))
        self.txt_link_mp4.setStyleSheet(u"background-color: white;")
        self.Button_descargar_mp4 = QPushButton(FormDos)
        self.Button_descargar_mp4.setObjectName(u"Button_descargar_mp4")
        self.Button_descargar_mp4.setGeometry(QRect(140, 160, 91, 31))
        self.Button_descargar_mp4.setStyleSheet(u"font: 87 8pt \"Arial Black\";\n"
"color: white;")
        self.pushButton_menu = QPushButton(FormDos)
        self.pushButton_menu.setObjectName(u"pushButton_menu")
        self.pushButton_menu.setGeometry(QRect(0, 0, 71, 23))
        self.pushButton_menu.setStyleSheet(u"color: white;\n"
"font: 87 10pt \"Arial Black\";")
        self.label = QLabel(FormDos)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 200, 251, 41))
        self.label.setStyleSheet(u"font: 87 14pt \"Arial Black\";\n"
"color: white;\n"
"border: 2px solid #555;")

        self.retranslateUi(FormDos)

        QMetaObject.connectSlotsByName(FormDos)
    # setupUi

    def retranslateUi(self, FormDos):
        FormDos.setWindowTitle(QCoreApplication.translate("FormDos", u"MP4", None))
        self.label_titulo_mp4.setText(QCoreApplication.translate("FormDos", u"Descarga MP4", None))
        self.label_link_mp4.setText(QCoreApplication.translate("FormDos", u"Insertar el Link de click y espere el mensaje:", None))
        self.Button_descargar_mp4.setText(QCoreApplication.translate("FormDos", u"Descargar", None))
        self.pushButton_menu.setText(QCoreApplication.translate("FormDos", u"Menu", None))
        self.label.setText("")
    # retranslateUi

