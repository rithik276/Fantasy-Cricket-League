from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_OpenWindow(object):
    def setupUi(self, OpenWindow):
        OpenWindow.setObjectName("OpenWindow")
        OpenWindow.resize(535, 389)
        font = QtGui.QFont()
        font.setFamily("Cantarell")
        font.setPointSize(12)
        OpenWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(OpenWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.OpenTeam = QtWidgets.QLabel(self.centralwidget)
        self.OpenTeam.setGeometry(QtCore.QRect(120, 120, 301, 20))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.OpenTeam.setFont(font)
        self.OpenTeam.setObjectName("OpenTeam")
        self.OpenTheTeam = QtWidgets.QLineEdit(self.centralwidget)
        self.OpenTheTeam.setGeometry(QtCore.QRect(130, 160, 261, 31))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.OpenTheTeam.setFont(font)
        self.OpenTheTeam.setObjectName("OpenTheTeam")
        self.openButton = QtWidgets.QPushButton(self.centralwidget)
        self.openButton.setGeometry(QtCore.QRect(210, 210, 93, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.openButton.setFont(font)
        self.openButton.setObjectName("openButton")
        OpenWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(OpenWindow)
        self.statusbar.setObjectName("statusbar")
        OpenWindow.setStatusBar(self.statusbar)

        self.retranslateUi(OpenWindow)
        QtCore.QMetaObject.connectSlotsByName(OpenWindow)

    def retranslateUi(self, OpenWindow):
        _translate = QtCore.QCoreApplication.translate
        OpenWindow.setWindowTitle(_translate("OpenWindow", "MainWindow"))
        self.OpenTeam.setText(_translate("OpenWindow", "Enter Team Name to Open:"))
        self.openButton.setText(_translate("OpenWindow", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OpenWindow = QtWidgets.QMainWindow()
    ui = Ui_OpenWindow()
    ui.setupUi(OpenWindow)
    OpenWindow.show()
    sys.exit(app.exec_())

