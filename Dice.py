from PyQt5 import QtCore, QtGui, QtWidgets


class Dice(QtWidgets.QLabel):
    def __init__(self, _parent: QtWidgets.QWidget, _pixmap: QtGui.QPixmap, _number: int):
        super().__init__()
        self.setParent(_parent)
        self.setPixmap(_pixmap)
        self.number: int = _number
        self.locked: bool = False
        self.first_round: bool = True

    def change_number(self, _number: int):
        self.number = _number
        self.setPixmap(QtGui.QPixmap("images/dice" + str(self.number) + ".png"))

    def change_locked(self, _locked: bool):
        if not self.first_round:
            if self.locked == _locked:
                raise AttributeError(f'Already assigned to {self.locked}')
            else:
                if self.locked:
                    self.setPixmap(QtGui.QPixmap("images/dice" + str(self.number) + ".png"))
                else:
                    self.setPixmap(QtGui.QPixmap("images/dice" + str(self.number) + "_locked.png"))
            self.locked = _locked

    def mousePressEvent(self, event):
        event.accept()
        if self.locked:
            self.change_locked(False)
        else:
            self.change_locked(True)
