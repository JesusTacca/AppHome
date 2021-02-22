from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtSql 
import sqlite3
def sql_connection():
    try:
        con = sqlite3.connect('Database/mydatabase.db')
        return con
    except Error:
        print(Error)

def Home(this):
    #Insert
    this.label_01 = QLabel(this)
    this.label_01.setText('Name')
    this.label_01.move(50,30)
    this.Edit_01 = QLineEdit(this)
    this.Edit_01.move(120,30)
    this.Edit_01.resize(120,30)

    this.label_02 = QLabel(this)
    this.label_02.setText("Surname")
    this.label_02.move(50,80)
    this.Edit_02 = QLineEdit(this)
    this.Edit_02.move(120,80)
    this.Edit_02.resize(120,30)

    this.label_03= QLabel(this)
    this.label_03.setText("DNI")
    this.label_03.move(50,130)
    this.Edit_03 = QLineEdit(this)
    this.Edit_03.setValidator(QIntValidator(10000000,99999999))
    this.Edit_03.move(120,130)
    this.Edit_03.resize(120,30)

    this.label_04 = QLabel(this)
    this.label_04.setText("Money")
    this.label_04.move(50,180)
    this.Edit_04 = QLineEdit(this)
    this.Edit_04.setValidator(QDoubleValidator(0.0,99999999,2))
    this.Edit_04.move(120,180)
    this.Edit_04.resize(120,30)

    this.label_05 = QLabel(this)
    this.label_05.setText("Email")
    this.label_05.move(350,30)
    this.Edit_05 = QLineEdit(this)
    this.Edit_05.move(450,30)
    this.Edit_05.resize(120,30)

    this.label_06 = QLabel(this)
    this.label_06.setText("Fecha de Nacimiento")
    this.label_06.move(350,80)
    this.label_06_1 = QLabel(this)
    this.label_06_1.setText("/")
    this.label_06_1.move(481,80)
    this.label_06_1.setFont(QFont("Arial",20))
    this.label_06_2 = QLabel(this)
    this.label_06_2.setText("/")
    this.label_06_2.move(521,80)
    this.label_06_2.setFont(QFont("Arial",20))
    this.Edit_06_1 = QLineEdit(this)
    this.Edit_06_1.move(450,80)
    this.Edit_06_1.resize(30,30)
    this.Edit_06_1.setValidator(QIntValidator(1,31))
    this.Edit_06_2 = QLineEdit(this)
    this.Edit_06_2.move(490,80)
    this.Edit_06_2.resize(30,30)
    this.Edit_06_2.setValidator(QIntValidator(1,12))
    this.Edit_06_3 = QLineEdit(this)
    this.Edit_06_3.move(530,80)
    this.Edit_06_3.resize(60,30)
    this.Edit_06_3.setValidator(QIntValidator())
    this.Edit_06_3.setMaxLength(4)

    this.label_07 = QLabel(this)
    this.label_07.setText("Numero")
    this.label_07.move(350,130)
    this.Edit_07 = QLineEdit(this)
    this.Edit_07.setValidator(QIntValidator(100000000,999999999))
    this.Edit_07.move(450,130)
    this.Edit_07.resize(120,30)

    this.label_08 = QLabel(this)
    this.label_08.setText("Contraseña")
    this.label_08.move(350,180)
    this.Edit_08 = QLineEdit(this)
    this.Edit_08.setEchoMode(QLineEdit.Password)
    this.Edit_08.move(450,180)
    this.Edit_08.resize(120,30)

    this.button = QPushButton('Agregar', this)
    this.button.move(600,100)
    this.button.resize(100,30)
    this.button.clicked.connect(this.Insert_User)
    #Table
    this.cur.execute("SELECT * FROM usuario")
    rows = this.cur.fetchall()
    print(rows)
    m = 0
    if len(rows)!=0:
        m = len(rows)
    print(m)
    this.tableWidget = QTableWidget(m,9)
    this.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
    info = []
    for i, a in enumerate(rows):
        for j, b in enumerate(a):
            this.tableWidget.setItem(i,j,QTableWidgetItem(str(b)))
    this.tableWidget.move(0,0)
    this.layout = QVBoxLayout()
    this.layout.addWidget(this.tableWidget) 
    this.main_widget.setLayout(this.layout)

class App(QMainWindow):
 
    def __init__(self):
        super().__init__()

        self.title = 'App Home'
        self.left = 300
        self.top = 50
        self.width = 750
        self.height = 650
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.main_widget = QWidget(self)
        self.main_widget.setContentsMargins(50, 200, 0, 0)
        self.main_widget.setFixedSize(700, 600)
        self.setCentralWidget(self.main_widget)
        # Database
        self.con = sql_connection()
        self.cur = self.con.cursor()
        # Menu bar
        #  Exit
        exitAction = QAction('&Exit', self)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        #  Home
        Home(self)
        #  Insert User

        #  Delete User

        #  Update User

        self.statusBar()
        self.show()
    @pyqtSlot()
    def Insert_User(self):
        txt = "insert into usuario(name, surname, DNI, money, email, fecha_nacimiento, numero, contrasena) values ('"+self.Edit_01.text()+"','"+self.Edit_02.text()+"',"+self.Edit_03.text()+","+self.Edit_04.text()+",'"+self.Edit_05.text()+"','"+self.Edit_06_1.text()+'/'+self.Edit_06_2.text()+'/'+self.Edit_06_3.text()+"',"+self.Edit_07.text()+",'"+self.Edit_08.text()+"')"
        self.cur.execute(txt)
        self.con.commit()
        temp=self.tableWidget.rowCount()
        self.tableWidget.insertRow(temp)
        self.tableWidget.setItem(temp,0,QTableWidgetItem(str(temp+1)))
        self.tableWidget.setItem(temp,1,QTableWidgetItem(self.Edit_01.text()))
        self.tableWidget.setItem(temp,2,QTableWidgetItem(self.Edit_02.text()))
        self.tableWidget.setItem(temp,3,QTableWidgetItem(self.Edit_03.text()))
        self.tableWidget.setItem(temp,4,QTableWidgetItem(self.Edit_04.text()))
        self.tableWidget.setItem(temp,5,QTableWidgetItem(self.Edit_05.text()))
        self.tableWidget.setItem(temp,6,QTableWidgetItem(self.Edit_06_1.text()+'/'+self.Edit_06_2.text()+'/'+self.Edit_06_3.text()))
        self.tableWidget.setItem(temp,7,QTableWidgetItem(self.Edit_07.text()))
        self.tableWidget.setItem(temp,8,QTableWidgetItem(self.Edit_08.text()))