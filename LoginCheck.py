from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5 import QtWidgets,uic
import sys

class LoginCheckClass(QDialog):
    def __init__(self):
        super(LoginCheckClass,self).__init__()
        uic.loadUi('loginform.ui',self)
        self.photolabel.setPixmap(QPixmap("login.jpg"))
        self.photolabel.setScaledContents(True)
        self.loginButton.clicked.connect(self.loginfun)

    def loginfun(self):
        username=self.usrtext.toPlainText().strip()
        password=self.pwdtxt.text().strip()

        #DB connect & query
        self.DBConnect()
        cursor=self.mydb.cursor()
        cursor.execute("select * from login_tb")
        rows=cursor.fetchall()
        found=0
        for x in rows:
            usr=x[1]
            pwd=x[2]
            if username==usr and password==pwd:
                found=1
                self.setVisible(False)
                from LibraryForm import LibrarySystem
                lib=LibrarySystem()
                lib.show()
                lib.exec_()

        if found==0:
            from PyQt5.QtWidgets import QMessageBox
            msg=QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Login unsuccessful, Try Again!")
            msg.setWindowTitle("Error Login")
            msg.exec()

    def DBConnect(self):
        import mysql.connector as c
        try:
            self.mydb=c.connect(
                host="localhost",
                user="root",
                password="root",
                database="librarydb"
            )
        except c.Error as err:
            print("Something went wrong: {}".format(err))

if __name__=="__main__":
    app=QtWidgets.QApplication([])
    win=LoginCheckClass()
    win.show()
    sys.exit(win.exec_())