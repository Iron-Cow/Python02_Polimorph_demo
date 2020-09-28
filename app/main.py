import sys
from models.vectors import Vector
from PyQt5.QtWidgets import QApplication
from gui.calcui import MainWindowVec

if __name__ == '__main__':
    # v1 = Vector(x=2, y=3)
    # v2 = Vector(x=6, y=1)
    #
    # print(v1)
    # print(v2)
    #
    # print(v1 + v2)
    # print(v1 - v2)
    app = QApplication([])
    win = MainWindowVec()
    win.show()

    sys.exit(app.exec())

