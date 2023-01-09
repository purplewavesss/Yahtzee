import sys
import MainWindow
import Game
from PyQt5 import QtWidgets


# Contains triggers that give functionality to the main menu.
def implement_triggers(window: MainWindow, game: Game):
    window.exit_action.triggered.connect(exit_action_triggered)
    window.new_game_action.triggered.connect(lambda: new_game_action_triggered(game))
    window.credits_action.triggered.connect(credits_action_triggered)


def exit_action_triggered():
    sys.exit()


def new_game_action_triggered(game: Game):
    game.game_end(False)
    for player in game.players:
        player.reset()


def credits_action_triggered():
    credits_message_box = QtWidgets.QMessageBox()
    credits_message_box.setWindowTitle("Credits")
    credits_message_box.setIcon(QtWidgets.QMessageBox.Information)
    credits_message_box.setText("Created by Gavin J. Grotegut\nBased on Yahtzee, a game by Milton Bradley\nCoded in "
                                "Python\nDesigned in Qt, a GUI framework for C++ and Python")
    credits_message_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
    credits_message_box.exec()
