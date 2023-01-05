from PyQt5 import QtWidgets
import Player
import PlayerLabel
import PointItem
import Dice


# Encapsulates a ScoreCard, which is a table that displays current and potential scores represented by PointItems.
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
        
    def point_item_clicked(self, item: PointItem):
        # Checks if function runs
        if item.get_status() == "potential" and item.player.can_click:
            item.change_point_value(int(item.text()))

            # Adds point values
            if self.name == "upper":
                item.player.upper_points += item.get_point_value()
            elif self.name == "lower":
                item.player.lower_points += item.get_point_value()
            item.player.total_points += item.get_point_value()

            # Change PointItem status
            item.set_status("selected")

            # Change player attributes
            item.player.combo_dict[item.combo] = False
            item.player.can_click = False
            item.player.clear_point_items()

            # Switch current player
            self.player_label.set_current_player(self.switch_player(item.player))

            # Unlock all dice
            for die in self.dice_list:
                if die.get_locked():
                    die.set_locked(False)
                die.setHidden(True)

    def switch_player(self, _player: Player) -> Player:
        if _player == self.player_list[0]:
            return self.player_list[1]
        else:
            return self.player_list[0]
