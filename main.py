
from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot
from ui_Reproductor import Ui_MainWindow
from ui_mp3 import Ui_FormUno
from ui_mp4 import Ui_FormDos
from pytube import YouTube #libreria para descargar videos

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #funciones de botones
        self.ui.Button_mp3.clicked.connect(self.ventanaAmp3)
        self.ui.Button_mp4.clicked.connect(self.ventanaAmp4)

    #ir ventana mp3
    @Slot()
    def ventanaAmp3(self):
        self.hide()
        mp3 = VentanaMP3(self)
        mp3.show()
        

    #ir ventana mp4
    @Slot()
    def ventanaAmp4(self):
        self.hide()
        mp4 = VentanaMP4(self)
        mp4.show()

#class ventana mp3
class VentanaMP3(QMainWindow):
    def __init__(self, parent=None):
        super(VentanaMP3, self).__init__(parent)
        self.fo = Ui_FormUno()
        self.fo.setupUi(self)
        #funciones botones
        self.fo.pushButton_back.clicked.connect(self.regresarMenu)
        self.fo.pushButton_mp3.clicked.connect(self.descargarAudioLink)

    
    #descargarmp3
    @Slot()
    def descargarAudioLink(self):
        link = self.fo.txt_link_mp3.text()
        video = YouTube(link)
        t=video.streams.get_audio_only()
        t.download("/Users/Lenovo/Downloads/musica")
        self.fo.label.setText("Descarga Completa")
        
        


    @Slot()
    def regresarMenu(self):
        #regresar a clase padre
        self.parent().show()
        self.close()


#clase ventana mp4
class VentanaMP4(QMainWindow):
    #parent = clase padre
    def __init__(self, parent=None):
        super(VentanaMP4, self).__init__(parent)
        self.fore = Ui_FormDos()
        self.fore.setupUi(self)
        #funciones botones
        self.fore.pushButton_menu.clicked.connect(self.regresarMenu)
        self.fore.Button_descargar_mp4.clicked.connect(self.descargarVideoLink)

    #descargar mp4
    @Slot()
    def descargarVideoLink(self):
        link = self.fore.txt_link_mp4.text()
        video = YouTube(link)
        video.streams.first().download("/Users/Lenovo/Downloads/videos")
        self.fore.label.setText("Descarga Completa")
        
    @Slot()
    def regresarMenu(self):
        #regresar a clase padre
        self.parent().show()
        self.close()