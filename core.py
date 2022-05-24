from PySide2.QtWidgets import QApplication
from main import MainWindow
import  sys

#app
app = QApplication(sys.argv)

#window
window = MainWindow()
window.show()


#exec app
sys.exit(app.exec_())