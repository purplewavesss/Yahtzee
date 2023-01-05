from PyQt5 import QtGui, QtWidgets


class Dice(QtWidgets.QLabel):
    def __init__(self, _parent: QtWidgets.QWidget, _pixmap: QtGui.QPixmap, _number: int):
        super().__init__()
        self.setParent(_parent)
        self.setPixmap(_pixmap)
        self.__number: int = _number
        self.__locked: bool = False
        self.first_round: bool = True

    def get_number(self) -> int:
        return self.__number

    def set_number(self, _number: int):
        self.__number = _number
        self.setPixmap(QtGui.QPixmap("images/dice" + str(self.__number) + ".png"))

    def get_locked(self) -> bool:
        return self.__locked

    def set_locked(self, _locked: bool):
        if not self.first_round:
            if self.__locked == _locked:
                raise AttributeError(f'Already assigned to {self.__locked}')
            else:
                if self.__locked:
                    self.setPixmap(QtGui.QPixmap("images/dice" + str(self.__number) + ".png"))
                else:
                    self.setPixmap(QtGui.QPixmap("images/dice" + str(self.__number) + "_locked.png"))
            self.__locked = _locked

    def mousePressEvent(self, event):
        event.accept()
        if self.__locked:
            self.set_locked(False)
        else:
            self.set_locked(True)
