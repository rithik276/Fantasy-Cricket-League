from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ScoreWindow(object):
    def setupUi(self, ScoreWindow):
        ScoreWindow.setObjectName("ScoreWindow")
        ScoreWindow.resize(471, 386)
        self.centralwidget = QtWidgets.QWidget(ScoreWindow)
        self.centralwidget.setInputMethodHints(QtCore.Qt.ImhNoEditMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.Score = QtWidgets.QLineEdit(self.centralwidget)
        self.Score.setGeometry(QtCore.QRect(110, 180, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Score.setFont(font)
        self.Score.setInputMethodHints(QtCore.Qt.ImhNoEditMenu|QtCore.Qt.ImhNoPredictiveText)
        self.Score.setReadOnly(True)
        self.Score.setObjectName("Score")
        self.teamscore = QtWidgets.QLabel(self.centralwidget)
        self.teamscore.setGeometry(QtCore.QRect(80, 130, 321, 31))
        font = QtGui.QFont()
        font.setFamily("DejaVu Math TeX Gyre")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.teamscore.setFont(font)
        self.teamscore.setObjectName("teamscore")
        ScoreWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ScoreWindow)
        self.statusbar.setObjectName("statusbar")
        ScoreWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ScoreWindow)
        QtCore.QMetaObject.connectSlotsByName(ScoreWindow)

    def retranslateUi(self, ScoreWindow):
        _translate = QtCore.QCoreApplication.translate
        ScoreWindow.setWindowTitle(_translate("ScoreWindow", "MainWindow"))
        self.teamscore.setText(_translate("ScoreWindow", "Your Team Score :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ScoreWindow = QtWidgets.QMainWindow()
    ui = Ui_ScoreWindow()
    ui.setupUi(ScoreWindow)
    ScoreWindow.show()
    sys.exit(app.exec_())

