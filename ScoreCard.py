import random

from PyQt5 import QtCore, QtGui, QtWidgets
from PointsItem import PointsItem
from Dice import Dice


class ScoreCard(QtWidgets.QTableWidget):
    def __init__(self, _parent: QtWidgets.QWidget, _name: str, _dice_list: list[Dice]):
        super().__init__()
        self.setParent(_parent)
        self.name: str = _name
        self.dice_list: list[Dice] = _dice_list
        self.itemClicked.connect(self.point_item_clicked)
        
    def point_item_clicked(self, item: PointsItem):
        if item.get_status() == "potential" and item.player.can_click:
            item.change_point_value(int(item.text()))
            if self.name == "upper":
                item.player.upper_points += item.get_point_value()
            elif self.name == "lower":
                item.player.lower_points += item.get_point_value()
            item.player.total_points += item.get_point_value()
            item.set_status("selected")
            item.player.combo_dict[item.combo] = False
            item.player.can_click = False
            item.player.clear_point_items()
            for die in self.dice_list:
                if die.get_locked():
                    die.set_locked(False)
                die.set_number(random.randint(1, 6))
