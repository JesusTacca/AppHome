from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QSQLITE

class App(QMainWindow):
 
    def __init__(self):
        super().__init__()

        self.title = 'App Home'
        self.left = 50
        self.top = 50
        self.width = 1250
        self.height = 650
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        # Menu bar

        # Crear cuadro de texto
        self.textbox = QTextEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(460,150)
        
        self.tb = QTextBrowser(self)
        self.tb.move(20, 260)
        self.tb.resize(460,150)

        self.actual = 0

        self.button = QPushButton('Vamos!', self)
        self.button.move(280,200)
        self.button.resize(200,30)

        self.cb = QComboBox(self)
        self.cb.move(20,200)
        self.cb.resize(200,30)
        self.cb.addItems(["MD4", "MD5", "SHA1", "SHA3 (224)", 
                        "SHA3 (256)", "SHA3 (384)", "SHA3 (512)", 
                        "SHA224", "SHA256", "SHA384", "SHA512", 
                        "RIPE Hash MD160", "BASE64(Codificar)", 
                        "BASE64(Decodificar)"])
        self.cb.currentIndexChanged.connect(self.selectionchange)
        
        self.button.clicked.connect(self.on_click)
        self.show()
    def selectionchange(self,i):
        self.actual = i
    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.toPlainText()
        self.tb.setText(textboxValue)