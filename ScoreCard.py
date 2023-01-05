from PyQt5 import QtWidgets
import Player
import PlayerLabel
import PointsItem
import Dice


class ScoreCard(QtWidgets.QTableWidget):
    def __init__(self, _parent: QtWidgets.QWidget, _name: str, _dice_list: list[Dice], _player_label: PlayerLabel,
                 _player_list: list[Player]):
        super().__init__()
        self.setParent(_parent)
        self.name: str = _name
        self.dice_list: list[Dice] = _dice_list
        self.player_list: list[Player] = _player_list
        self.player_label: PlayerLabel = _player_label
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
            self.player_label.set_current_player(self.switch_player(item.player))
            for die in self.dice_list:
                if die.get_locked():
                    die.set_locked(False)
            for x in range(len(self.dice_list)):
                self.dice_list[x].set_number(x + 1)

    def switch_player(self, _player: Player) -> Player:
        if _player == self.player_list[0]:
            return self.player_list[1]
        else:
            return self.player_list[0]
