from PyQt5 import QtWidgets, QtCore
from untitled import Ui_MainWindow
from math import sqrt
import sys

class mywindow(QtWidgets.QMainWindow):


    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Calculator")

        self.ui.pushButton.clicked.connect(self.btnClicked_1)
        self.ui.pushButton_2.clicked.connect(self.btnClicked_2)
        self.ui.pushButton_3.clicked.connect(self.btnClicked_3)
        self.ui.pushButton_4.clicked.connect(self.btnClicked_4)
        self.ui.pushButton_5.clicked.connect(self.btnClicked_5)
        self.ui.pushButton_6.clicked.connect(self.btnClicked_6)
        self.ui.pushButton_7.clicked.connect(self.btnClicked_7)
        self.ui.pushButton_8.clicked.connect(self.btnClicked_8)
        self.ui.pushButton_9.clicked.connect(self.btnClicked_9)
        self.ui.pushButton_10.clicked.connect(self.btnClicked_10)
        self.ui.pushButton_11.clicked.connect(self.btnClicked_11)
        self.ui.pushButton_12.clicked.connect(self.btnClicked_12)
        self.ui.pushButton_13.clicked.connect(self.btnClicked_13)
        self.ui.pushButton_14.clicked.connect(self.btnClicked_14)
        self.ui.pushButton_15.clicked.connect(self.btnClicked_15)
        self.ui.pushButton_16.clicked.connect(self.btnClicked_16)
        self.ui.pushButton_17.clicked.connect(self.btnClicked_17)


    def btnClicked_1(self):
        self.textbox = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(self.textbox + " + ")

    def btnClicked_2(self):
        self.textbox = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(self.textbox + " * ")

    def btnClicked_3(self):
        self.textbox = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(self.textbox + " / ")

    def btnClicked_4(self):
        self.textbox = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(str(result))

    def btnClicked_5(self):
        self.textbox = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(self.textbox + " - ")

    def btnClicked_6(self):
        self.textbox = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(self.textbox + " = ")
        term = self.textbox.split( )
        global result
        result = int(term[0])
        for i in range(1, len(term), 2):
            if term[i] == '+':
                result = result + int(term[i+1])

            if term[i] == '-':
                result = result - int(term[i+1])

            if term[i] == '*':
                result = result * int(term[i+1])

            if term[i] == '/':
                result = result / int(term[i+1])

        self.textbox = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(self.textbox + str(result))

    def btnClicked_7(self):
        self.textbox = self.ui.lineEdit.text()
        self.ui.lineEdit.setText("")
        global result
        result = 0

    def btnClicked_8(self):
        self.textbox = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(self.textbox + "4")

    def btnClicked_9(self):
        self.textbox = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(self.textbox + "1")

    def btnClicked_10(self):
        self.textbox = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(self.textbox + "7")

    def btnClicked_11(self):
        self.textbox = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(self.textbox + "2")

    def btnClicked_12(self):
        self.textbox = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(self.textbox + "3")

    def btnClicked_13(self):
        self.textbox = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(self.textbox + "5")

    def btnClicked_14(self):
        self.textbox = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(self.textbox + "6")

    def btnClicked_15(self):
        self.textbox = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(self.textbox + "8")

    def btnClicked_16(self):
        self.textbox = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(self.textbox + "9")

    def btnClicked_17(self):
        self.textbox = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(self.textbox + "0")


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())