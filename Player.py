# Encapsulates the concept of a player, including what items in the ScoreCard are assigned to them.
class Player:
    def __init__(self, _player_num: int):
        self.player_num: int = _player_num
        self.roll_num: int = 0
        # Dictionary containing pairs of combo name and if the combo has already been used
        self.combo_dict: dict[str, bool] = {}
        self.has_yahtzee: bool = False
        self.has_bonus: bool = False
        self.can_click: bool = True
        self.round_finished: bool = False
        self.upper_points: int = 0
        self.lower_points: int = 0
        self.total_points: int = 0
        self.point_items_list: list[PointItem] = []

    def clear_potential_point_items(self):
        for point_item in self.point_items_list:
            status = point_item.get_status()
            if status == "potential":
                point_item.set_status("hidden")

    def erase_point_items(self):
        for point_item in self.point_items_list:
            point_item.set_status("hidden")
            point_item.set_point_value(0)

    def reset(self):
        self.roll_num: int = 0
        self.has_yahtzee = False
        self.has_bonus = False
        self.can_click = True
        self.round_finished = False
        self.upper_points = 0
        self.lower_points = 0
        self.total_points = 0


# This is the dumbest fix I have ever done
import PointItem
