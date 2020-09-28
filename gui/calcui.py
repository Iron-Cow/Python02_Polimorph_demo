from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox

from models.vectors import Vector


class MainWindowVec(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.__win = uic.loadUi('../templates/calc.ui')

    def set_slots(self):
        self.__win.pushButton_result.clicked.connect(self.slot1)

    def show(self) -> None:
        self.set_slots()
        self.__win.show()

    def slot1(self):
        '''Action for push button'''
        try:
            x = float(self.__win.lineEdit_1.text())
            y = float(self.__win.lineEdit_2.text())
            v = Vector(x, y)
            v_2 = Vector(1, 1)
            v_result = v + v_2
            self.__win.lineEdit_result.setText(str(v_result))
        except ValueError:
            # QMessageBox.information(self, 'ERRROr', 'Вводить только числа!')
            QMessageBox.warning(self, 'ERRROr', 'Вводить только числа!')
            QMessageBox.critical(self, 'ERRROr', 'Вводить только числа!')
            QMessageBox.question(self, 'ERRROr', 'Вводить только числа!')

