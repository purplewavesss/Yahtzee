from PyQt5 import QtGui, QtWidgets
import Player

NOT_COMBO: tuple = ("Total Score", "Total", "Total (Lower)", "Total (Upper)", "Grand Total")


# Encapsulates a PointItem, which is a table item containing a point value. This point value can be hidden or shown
# based on the results of the last dice roll.
class PointItem(QtWidgets.QTableWidgetItem):
    def __init__(self, _combo: str, _player: Player):
        super().__init__()
        self.combo: str = _combo
        self.player: Player = _player
        self.__point_value: int = 0
        self.__status: str = "hidden"
        self.player.points_items_list.append(self)
        self.add_to_combo_dict()
        self.setText("")

    def get_status(self) -> str:
        return self.__status

    def set_status(self, _status: str):
        self.__status = _status
        match self.__status:
            # No text visible, no point value shown
            case "hidden":
                self.setText("")
            # Red text and point value visible, shows when there is a possible combo the player can choose
            case "potential":
                self.setText(str(self.__point_value))
                self.setForeground(QtGui.QBrush(QtGui.QColor(255, 0, 0)))
                self.player.combo_dict[self.combo] = True
            # Normal text and point value visible, shows after a user selects a combo
            case "selected":
                self.setText(str(self.__point_value))
                self.setForeground(QtGui.QBrush(QtGui.QColor(0, 0, 0)))
                self.player.combo_dict[self.combo] = False

    def get_point_value(self):
        return self.__point_value

    def set_point_value(self, _point_value: int):
        self.__point_value = _point_value
        if self.__status != "hidden":
            self.setText(str(self.__point_value))

    def add_to_combo_dict(self):
        if self.combo not in NOT_COMBO:
            self.player.combo_dict.update({self.combo: True})
