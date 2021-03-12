from PyQt5 import QtWidgets, QtCore
from untitled import Ui_MainWindow
import sys

class mywindow(QtWidgets.QMainWindow):

        def __init__(self):
                super(mywindow, self).__init__()
                self.ui = Ui_MainWindow()
                self.ui.setupUi(self)
                self.setWindowTitle("Temperature")

                self.ui.pushButton.clicked.connect(self.btnClicked)

                self.first = self.ui.lineEdit
                self.second = self.ui.lineEdit_2
                self.third = self.ui.lineEdit_3
                self.fourth = self.ui.lineEdit_4
                self.fifth = self.ui.lineEdit_5


        def btnClicked(self):
                first = int(self.first.text())
                second = int(self.second.text())
                third = int(self.third.text())
                fourth = int(self.fourth.text())
                fifth = int(self.fifth.text())

                amount = (first + second + third + fourth + fifth) / 5
                self.ui.lineEdit_6.setText(str(amount))

app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())