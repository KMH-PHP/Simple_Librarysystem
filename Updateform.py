from PyQt5.QtWidgets import QDialog
from PyQt5 import QtWidgets,uic
import sys
import mysql.connector as sql 

class UpdatFormUI(QDialog):
    def __init__(self,bid):
        super(UpdatFormUI,self).__init__()
        uic.loadUi('updateform.ui',self)
        self.mydb=None
        print("the bookid is :"+str(bid))
        self.LoadData(bid)
        self.updateBut.clicked.connect(self.Update)
        self.insertBut.clicked.connect(self.InsertData)
        self.deleteBut.clicked.connect(self.DeleteData)
        self.clearBut.clicked.connect(self.ClearData)

    def Update(self):
       id= self.idtxt.toPlainText()
       title = self.titletxt.toPlainText()
       author =self.authortxt.toPlainText()
       publisher=self.publishertxt.toPlainText()
       year= self.yeartxt.toPlainText()
       copy= self.copytxt.toPlainText()
       leftcopy= self.leftcopytxt.toPlainText()
       self.DBConnect()
       cursor=self.mydb.cursor()
       sql_update="update book_tb set title=%s,author=%s,publisher=%s,published_year=%s,num_copies=%s,left_copies=%s where book_id="+str(id)
       value=(title,author,publisher,year,copy,leftcopy)
       cursor.execute(sql_update,value)
       self.mydb.commit()
       self.showMessageText("Update Successfully", "OK")
    def showMessageText(self,body,title):
       from PyQt5.QtWidgets import QMessageBox
       msg=QMessageBox()
       msg.setText(body)
       msg.setWindowTitle(title)
       msg.exec_()


    def InsertData(self):
       id= self.idtxt.toPlainText()
       title = self.titletxt.toPlainText()
       author =self.authortxt.toPlainText()
       publisher=self.publishertxt.toPlainText()
       year= self.yeartxt.toPlainText()
       copy= self.copytxt.toPlainText()
       leftcopy= self.leftcopytxt.toPlainText()
       self.DBConnect()
       cursor=self.mydb.cursor()
       insert_sql="insert into book_tb(book_id,title,author,publisher,published_year,num_copies,left_copies) values(%s,%s,%s,%s,%s,%s,%s)"
       value=(id,title,author,publisher,year,copy,leftcopy)
       cursor.execute(insert_sql,value)
       self.mydb.commit()
       self.ClearData()
       self.showMessageText("Insert successfully", "done")

    def DeleteData(self):
        id= self.idtxt.toPlainText()
        if len(id)==0:
            self.showMessageText("Enter book id to delete", "No Data Error")
        else:
            self.DBConnect()
            cursor=self.mydb.cursor()
            delete_str="delete from book_tb where book_id ="+str(id)
            cursor.execute(delete_str)
            self.mydb.commit()
            self.ClearData()
            self.showMessageText("Deletion data is successfully done","OK")

    def ClearData(self):
        self.idtxt.setPlainText("")
        self.titletxt.setPlainText("")
        self.authortxt.setPlainText("")
        self.publishertxt.setPlainText("")
        self.yeartxt.setPlainText("")
        self.copytxt.setPlainText("")
        self.leftcopytxt.setPlainText("")

    def LoadData(self,bid):
        self.DBConnect()
        sql="select * from book_tb where book_id="+str(bid)
        cursor=self.mydb.cursor()
        cursor.execute(sql)
        values=cursor.fetchone()
        self.idtxt.setPlainText(str(values[1]))
        self.titletxt.setPlainText(str(values[2]))
        self.authortxt.setPlainText(str(values[3]))
        self.publishertxt.setPlainText(str(values[4]))
        self.yeartxt.setPlainText(str(values[5]))
        self.copytxt.setPlainText(str(values[6]))
        self.leftcopytxt.setPlainText(str(values[7]))
        
        
        
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
            print("Something went wrong:")


"""if __name__=="__main__":
    app=QtWidgets.QApplication([])
    win=UpdatFormUI(2012)
    win.show()
    sys.exit(win.exec_())"""