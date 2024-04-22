import mysql.connector
import sys

from PyQt6 import QtCore, uic, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "c97bengjeqde!@",
    database = "levtest"
)

mycursor = db.cursor()

mycursor.execute("SELECT * FROM TestAssetList")

toDisplay = []
for row in mycursor:
    toDisplay.append(list(row))

class TableModel1(QtCore.QAbstractTableModel):
    def __init__(self,data):
        super(TableModel1, self).__init__()
        self._data = data

    def data(self,index,role):
        if role == Qt.ItemDataRole.DisplayRole:
            return str(self._data[index.row()][index.column()])
        return None
    
    def rowCount(self,index):
        return len(self._data)
    
    def columnCount(self, index):
        return len(self._data[0])

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        self.table = QtWidgets.QTableView()

        data = toDisplay
        self.model = TableModel1(data)
        self.table.setModel(self.model)

        self.setCentralWidget(self.table)



app = QApplication(sys.argv)

window = MainWindow()
#window = uic.loadUi(r"C:\Users\worki\OneDrive\Documents\Coding\Resource Manager\secondTest.ui")
window.show()
app.exec()





db.close()