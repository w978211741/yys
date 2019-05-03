#encoding=utf-8
from MainWindow import My_MainWindow
from PyQt5 import QtWidgets
import sys


if __name__ == "__main__":
    print("开始")
    app = QtWidgets.QApplication(sys.argv)
    my_pyqt_form = My_MainWindow()
    my_pyqt_form.show()
    sys.exit(app.exec_())


