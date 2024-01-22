from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5 import QtWidgets,uic
import sys
import mysql.connector as sql 

class LibrarySystem(QDialog):
    def __init__(self):
        super(LibrarySystem,self).__init__()
        self.mydb=None
        uic.loadUi('Librayform.ui',self)

        self.search.clicked.connect(self.SearchBook)
        self.tableView.clicked.connect(self.TableSelect)
        self.updateBut.clicked.connect(self.UpdateData)

    def UpdateData(self):

        index= self.tableView.selectionModel().currentIndex()
        value=index.sibling(index.row(),index.column()).data()
        self.setVisible(False)
        from Updateform import UpdatFormUI
        ui=UpdatFormUI(value)
        ui.show()
        ui.exec_()
    def TableSelect(self):
        self.updateBut.setEnabled(True)

    def SearchBook(self):
        choosetype=None
        datainput=None
        if self.radioauthor.isChecked():
            choosetype="author"
        elif self.radiotitle.isChecked():
            choosetype="title"
        else:
            
            choosetype="publisher"

        datainput=self.inputtxt.toPlainText().strip()
        print(choosetype)
        print(datainput)

        sql_str="select * from book_tb where "+choosetype+" = '"+datainput+"'"
        print(sql_str)

        self.DBConnect()
        cursor = self.mydb.cursor()
        cursor.execute(sql_str)
        rows = cursor.fetchall()

        if len(rows) == 0:
            from PyQt5.QtWidgets import QMessageBox
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Your information is not found , Try another search.")
            msg.setWindowTitle("No Data")
            msg.exec_()
            
        else:
           import pandas as pd
           sql_query=pd.read_sql(sql_str,self.mydb)
           df=pd.DataFrame(sql_query,columns=['id','book_id','title','author','publisher','pulished_year','num_copies','left_copies'])
           from TableModel import pandasModel
           model=pandasModel(df)
           self.tableView.setModel(model)
           print(df)

    def DBConnect(self):
        try:
            self.mydb=sql.connect(
                host = "localhost",
                user = "root",
                password = "root",
                database = "librarydb"
            )
        except:
             
             print("DB error")   
