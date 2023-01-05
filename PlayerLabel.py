from PyQt5 import QtWidgets
import Player


class PlayerLabel(QtWidgets.QLabel):
    def __init__(self, _parent: QtWidgets.QWidget, _current_player: Player):
        super().__init__()
        self.setParent(_parent)
        self.__current_player = _current_player

    def get_current_player(self) -> Player:
        return self.__current_player

    def set_current_player(self, _player):
        self.__current_player = _player
        self.setText(f'Player {self.__current_player.player_num}!')
