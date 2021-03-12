from PyQt5 import QtWidgets, QtCore
from untitled import Ui_MainWindow
import sys

class mywindow(QtWidgets.QMainWindow):

    def __init__(self):
            super(mywindow, self).__init__()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.setWindowTitle("Run")

            self.ui.pushButton.clicked.connect(self.btnClicked)

            self.firstday = self.ui.lineEdit
            self.secondday = self.ui.lineEdit_2
            self.thirdday = self.ui.lineEdit_3
            self.fourthday = self.ui.lineEdit_4
            self.fifthday = self.ui.lineEdit_5


    def btnClicked(self):
                firstday = int(self.firstday.text())
                secondday = int(self.secondday.text())
                thirdday = int(self.thirdday.text())
                fourthday = int(self.fourthday.text())
                fifthday = int(self.fifthday.text())


                days = [firstday, secondday, thirdday, fourthday, fifthday]
                allrun = firstday + secondday + thirdday + fourthday + fifthday
                amountrun = allrun / 5

                minrun = days[0]
                for i in range(0, 5):
                    if minrun > days[i]:
                        minrun = days[i]

                maxrun = days[0]

                for i in range(0, 5):
                    if maxrun < days[i]:
                            maxrun = days[i]

                self.ui.lineEdit_6.setText(str(allrun))
                self.ui.lineEdit_7.setText(str(amountrun))

                self.ui.lineEdit_8.setText(str(minrun))
                self.ui.lineEdit_9.setText(str(maxrun))




app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())