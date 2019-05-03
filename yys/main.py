#encoding=utf-8
from MainWindow import My_MainWindow
from PyQt5 import QtWidgets
import sys
import multiprocessing

def main():
    print("开始")
    multiprocessing.freeze_support()
    app = QtWidgets.QApplication(sys.argv)
    my_pyqt_form = My_MainWindow()
    my_pyqt_form.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


