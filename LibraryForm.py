from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5 import QtWidgets,uic
import sys

class LibrarySystem(QDialog):
    def __init__(self):
        super(LibrarySystem,self).__init__()
        uic.loadUi('Librayform.ui',self)

        self.search.clicked.connect(self.SearchBook)

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

"""if __name__=="__main__":
    app=QtWidgets.QApplication([])
    win=LibrarySystem()
    win.show()
    sys.exit(win.exec_())"""