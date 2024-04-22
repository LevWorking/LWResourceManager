import mysql.connector
import sys
import PyQt6

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget




app = QApplication(sys.argv)

window = uic.loadUi(r"C:\Users\worki\OneDrive\Documents\Coding\Resource Manager\secondTest.ui")
window.show()
app.exec()



db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "c97bengjeqde!@",
    database = "levtest"
)

mycursor = db.cursor()

#Creates a table with stuff in it. 
#mycursor.execute("CREATE TABLE TestAssetList (name VARCHAR(50), description VARCHAR(100), filepath VARCHAR(200), assetID int PRIMARY KEY AUTO_INCREMENT)")

#nameEntry = "Crab_Asset"
#descEntry = "A powerful unit to conquer your foes."
#filepathEntry = r"C:\Users\worki\OneDrive\Documents\Coding\Resource Manager\Crab_Asset.jpeg"

#mycursor.execute("INSERT INTO TestAssetList (name, description, filepath) VALUES (%s, %s, %s)", (nameEntry, descEntry, filepathEntry) )
#db.commit()



mycursor.execute("SELECT * FROM TestAssetList")
for row in mycursor:
    name = row[0]
    description = row[1]
    filepath = row[2]
    assetID = row[3]

    print(name)

'''class Login(QWidget):
    def __init__(self):
        super().__init__()

        # use the Ui_login_form
        self.ui = "secondTest.ui"       
        self.ui.setupUi(self)       
        
        # show the login window
        self.show()'''
    

'''if __name__ == '__main__':
    app = QApplication(sys.argv)
    #login_window = Login()
    sys.exit(app.exec())'''

db.close()