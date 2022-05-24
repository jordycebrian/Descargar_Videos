# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Reproductor.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(231, 350)
        icon = QIcon()
        icon.addFile(u"../Downloads/icons8-carpeta-de-pel\u00edculas-96.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: #555;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_logo = QLabel(self.centralwidget)
        self.label_logo.setObjectName(u"label_logo")
        self.label_logo.setGeometry(QRect(16, 13, 201, 141))
        self.label_logo.setStyleSheet(u"font: 87 100pt \"Arial Black\";\n"
"background-color: white;\n"
"border: 2px solid #ccc\n"
"")
        self.Button_mp3 = QPushButton(self.centralwidget)
        self.Button_mp3.setObjectName(u"Button_mp3")
        self.Button_mp3.setGeometry(QRect(60, 180, 111, 31))
        self.Button_mp3.setStyleSheet(u"font: 87 8pt \"Arial Black\";\n"
"color: white;")
        self.Button_mp4 = QPushButton(self.centralwidget)
        self.Button_mp4.setObjectName(u"Button_mp4")
        self.Button_mp4.setGeometry(QRect(60, 240, 111, 31))
        self.Button_mp4.setStyleSheet(u"font: 87 8pt \"Arial Black\";\n"
"color: white;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 231, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DownloadYouTube", None))
        self.label_logo.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.Button_mp3.setText(QCoreApplication.translate("MainWindow", u"Descargar MP3", None))
        self.Button_mp4.setText(QCoreApplication.translate("MainWindow", u"Descargar MP4", None))
    # retranslateUi

