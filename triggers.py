import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from MainWindow import MainWindow


def implement_triggers(window: MainWindow):
    window.exit_action.triggered.connect(lambda: exit_action_triggered())
    window.credits_action.triggered.connect(lambda: credits_action_triggered())


def exit_action_triggered():
    sys.exit()


def credits_action_triggered():
    credits_message_box = QtWidgets.QMessageBox()
    credits_message_box.setWindowTitle("Credits")
    credits_message_box.setIcon(QtWidgets.QMessageBox.Information)
    credits_message_box.setText("Created by Gavin J. Grotegut\nBased on Yahtzee, a game by Milton Bradley")
    credits_message_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
    credits_message_box.exec()
