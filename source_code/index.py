from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sqlite3
import datetime
import sys
from xlrd import *
from xlsxwriter import *
from PyQt5.uic import loadUiType
from login import Ui_Form
from library import Ui_MainWindow


class Login(QWidget, Ui_Form):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.pushButton_l.clicked.connect(self.handle_login)

    def handle_login(self):
        db = sqlite3.connect('library.sqlite')
        cursor = db.cursor()

        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        print("Here")
        cursor.execute("""SELECT * FROM user """)
        data = cursor.fetchall()
        flag = 0
        for row in data:
            if username == row[1] and password == row[3]:
                self.window2 = MainApp()
                self.close()
                self.window2.show()

            else:
                self.label_2.setText("Incorrect Username or Password")


def main():

    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec_()

   



if __name__ == '__main__':
    main()
