import sqlite3
import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtWidgets import *


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.add_form = None
        self.con = sqlite3.connect('coffee.sqlite')
        self.cur = self.con.cursor()
        uic.loadUi('main.ui', self)
        layout = QVBoxLayout(self.centralWidget())
        self.tableWidget = QTableWidget(self)
        layout.addWidget(self.tableWidget)
        self.update_table()

    def update_table(self):
        query = """SELECT * FROM Coffee"""
        data = self.cur.execute(query).fetchall()
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(len(data[0]))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(
            ['id', 'название сорта', 'степень обжарки', 'молотый/в зернах', 'описание вкуса', 'цена', 'объем упаковки'])
        for i, row in enumerate(data):
            self.tableWidget.insertRow(i)
            for j, value in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(value)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    app.exec()
