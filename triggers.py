import sys
from PyQt5 import QtWidgets
import MainWindow


# Contains triggers that give functionality to the main menu.
def implement_triggers(window: MainWindow):
    window.exit_action.triggered.connect(exit_action_triggered)
    window.new_game_action.triggered.connect(new_game_action_triggered)
    window.credits_action.triggered.connect(credits_action_triggered)


def exit_action_triggered():
    sys.exit()


def new_game_action_triggered():
    # TODO: Add new game functionality
    raise NotImplementedError


def credits_action_triggered():
    credits_message_box = QtWidgets.QMessageBox()
    credits_message_box.setWindowTitle("Credits")
    credits_message_box.setIcon(QtWidgets.QMessageBox.Information)
    credits_message_box.setText("Created by Gavin J. Grotegut\nBased on Yahtzee, a game by Milton Bradley\nCoded in "
                                "Python\nDesigned in Qt, a GUI framework for C++ and Python")
    credits_message_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
    credits_message_box.exec()
