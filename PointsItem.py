from PyQt5 import QtCore, QtGui, QtWidgets
from Player import Player

not_combo: tuple = ("Total Score", "Total", "Total (Lower)", "Total (Upper)", "Grand Total")


class PointsItem(QtWidgets.QTableWidgetItem):
    def __init__(self, _combo: str, _player: Player):
        super().__init__()
        self.combo: str = _combo
        self.player: Player = _player
        self.point_value: int = 0
        self.status: str = "hidden"
        self.player.points_items_list.append(self)
        self.add_to_combo_dict()
        self.setText("")

    def change_status(self, _status: str):
        self.status = _status
        match self.status:
            # No text visible, no point value shown
            case "hidden":
                self.setText("")
            # Red text and point value visible, shows when there is a possible combo the player can choose
            case "potential":
                self.setText(str(self.point_value))
                self.setForeground(QtGui.QBrush(QtGui.QColor(255, 0, 0)))
                self.player.combo_dict[self.combo] = True
            # Normal text and point value visible, shows after a user selects a combo
            case "selected":
                self.setText(str(self.point_value))
                self.setForeground(QtGui.QBrush(QtGui.QColor(0, 0, 0)))
                self.player.combo_dict[self.combo] = False

    def change_point_value(self, _point_value: int):
        self.point_value = _point_value
        if self.status != "hidden":
            self.setText(str(self.point_value))

    def add_to_combo_dict(self):
        if self.combo not in not_combo:
            self.player.combo_dict.update({self.combo: True})
