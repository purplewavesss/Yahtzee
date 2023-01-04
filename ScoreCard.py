from PyQt5 import QtCore, QtGui, QtWidgets
from Player import Player
from PointsItem import PointsItem


class ScoreCard(QtWidgets.QTableWidget):
    def __init__(self, _parent: QtWidgets.QWidget, _name: str):
        super().__init__()
        self.setParent(_parent)
        self.name = _name
        self.itemClicked.connect(self.point_item_clicked)
        
    def point_item_clicked(self, item: PointsItem):
        if item.status == "potential" and item.player.can_click:
            item.point_value = int(item.text())
            if self.name == "upper":
                item.player.upper_points += item.point_value
            elif self.name == "lower":
                item.player.lower_points += item.point_value
            item.player.total_points += item.point_value
            item.change_status("selected")
            item.player.combo_dict[item.combo] = False
            item.player.can_click = False
            item.player.clear_point_items()
