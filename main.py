# pyuic5 des.ui -o des.py
# pyinstaller -F -w main.py
import datetime
import sys
from des import *


class handler(QtCore.QObject):
    sig_1 = QtCore.pyqtSignal(str)

    def run(self):
        while True:
            self.tm = datetime.datetime.now()
            self.S0 = int(self.tm.second % 10)
            self.S1 = int(self.tm.second / 10)
            self.M0 = int(self.tm.minute % 10)
            self.M1 = int(self.tm.minute / 10)
            self.H0 = int(self.tm.hour % 10)
            self.H1 = int(self.tm.hour / 10)
            self.sig_1.emit(f'{self.H1}{self.H0}:{self.M1}{self.M0}:{self.S1}{self.S0}')
            QtCore.QThread.msleep(1000)


class GUI(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.thread = QtCore.QThread()
        self.handler = handler()
        self.handler.moveToThread(self.thread)
        self.handler.sig_1.connect(self.prnt)
        self.thread.started.connect(self.handler.run)
        self.thread.start()

    def prnt(self, value):
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit.appendPlainText(value)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = GUI()
    myapp.show()
    sys.exit(app.exec_())
