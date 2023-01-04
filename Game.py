import random
from ComboChecker import ComboChecker
from Dice import Dice
from MainWindow import MainWindow
from Player import Player
from PointsItem import PointsItem


def table_dict_display(item: PointsItem, points: int):
    item.change_status("potential")
    item.setText(str(points))


class Game:
    def __init__(self, _window: MainWindow, _players: list[Player]):
        self.window = _window
        self.players = _players
        self.current_player: Player = self.players[0]
        self.dice_list: list[Dice] = [self.window.dice_1, self.window.dice_2, self.window.dice_3, self.window.dice_4,
                                      self.window.dice_5]
        self.combo_checker: ComboChecker = ComboChecker(self.dice_list, self.current_player)

    def roll(self):
        self.current_player.roll_num += 1
        self.current_player.clear_point_items()
        for die in self.dice_list:
            if die.first_round:
                die.first_round = False
            if not die.locked:
                die.change_number(random.randint(1, 6))
        self.display_items()
        if self.current_player.roll_num > 3 or not self.current_player.can_click:
            self.current_player.clear_point_items()
            if self.current_player.player_num == 1:
                self.change_current_player(self.players[1])
            else:
                self.change_current_player(self.players[0])
            self.current_player.roll_num = 0
            self.current_player.can_click = True

    def change_current_player(self, _current_player: Player):
        self.current_player = _current_player
        self.window.player_label.setText(f'Player {self.current_player.player_num}!')
        self.combo_checker.current_player = self.current_player

    def display_items(self):
        table_dict = self.combo_checker.generate_table_dict()
        for combo in table_dict.keys():
            if self.current_player.player_num == 1:
                match combo:
                    case 'Aces':
                        table_dict_display(self.window.aces_player_one, table_dict[combo])
                    case 'Twos':
                        table_dict_display(self.window.twos_player_one, table_dict[combo])
                    case 'Threes':
                        table_dict_display(self.window.threes_player_one, table_dict[combo])
                    case 'Fours':
                        table_dict_display(self.window.fours_player_one, table_dict[combo])
                    case 'Fives':
                        table_dict_display(self.window.fives_player_one, table_dict[combo])
                    case 'Sixes':
                        table_dict_display(self.window.sixes_player_one, table_dict[combo])
                    case '3 of a Kind':
                        table_dict_display(self.window.three_of_a_kind_player_one, table_dict[combo])
                    case '4 of a Kind':
                        table_dict_display(self.window.four_of_a_kind_player_one, table_dict[combo])
                    case 'Full House':
                        table_dict_display(self.window.full_house_player_one, table_dict[combo])
                    case 'Small Straight':
                        table_dict_display(self.window.small_straight_player_one, table_dict[combo])
                    case 'Large Straight':
                        table_dict_display(self.window.large_straight_player_one, table_dict[combo])
                    case 'Yahtzee':
                        table_dict_display(self.window.yahtzee_player_one, table_dict[combo])
                    case 'Chance':
                        table_dict_display(self.window.chance_player_one, table_dict[combo])
                    case 'Yahtzee Bonus':
                        table_dict_display(self.window.yahtzee_bonus_player_one, table_dict[combo])
            else:
                match combo:
                    case 'Aces':
                        table_dict_display(self.window.aces_player_two, table_dict[combo])
                    case 'Twos':
                        table_dict_display(self.window.twos_player_two, table_dict[combo])
                    case 'Threes':
                        table_dict_display(self.window.threes_player_two, table_dict[combo])
                    case 'Fours':
                        table_dict_display(self.window.fours_player_two, table_dict[combo])
                    case 'Fives':
                        table_dict_display(self.window.fives_player_two, table_dict[combo])
                    case 'Sixes':
                        table_dict_display(self.window.sixes_player_two, table_dict[combo])
                    case '3 of a Kind':
                        table_dict_display(self.window.three_of_a_kind_player_two, table_dict[combo])
                    case '4 of a Kind':
                        table_dict_display(self.window.four_of_a_kind_player_two, table_dict[combo])
                    case 'Full House':
                        table_dict_display(self.window.full_house_player_two, table_dict[combo])
                    case 'Small Straight':
                        table_dict_display(self.window.small_straight_player_two, table_dict[combo])
                    case 'Large Straight':
                        table_dict_display(self.window.large_straight_player_two, table_dict[combo])
                    case 'Yahtzee':
                        table_dict_display(self.window.yahtzee_player_two, table_dict[combo])
                    case 'Chance':
                        table_dict_display(self.window.chance_player_two, table_dict[combo])
                    case 'Yahtzee Bonus':
                        table_dict_display(self.window.yahtzee_bonus_player_two, table_dict[combo])
        if self.current_player.has_bonus:
            if self.current_player.player_num == 1:
                self.window.total_player_one.change_point_value(self.current_player.upper_points + 35)
                self.window.total_upper_player_one.change_point_value(self.current_player.upper_points + 35)
            else:
                self.window.total_player_two.change_point_value(self.current_player.upper_points + 35)
                self.window.total_upper_player_two.change_point_value(self.current_player.upper_points + 35)
        else:
            self.window.total_upper_player_one.change_point_value(self.players[0].upper_points)
            self.window.total_upper_player_two.change_point_value(self.players[1].upper_points)

        self.window.total_score_player_one.change_point_value(self.players[0].upper_points)
        self.window.total_score_player_two.change_point_value(self.players[1].upper_points)
        self.window.total_lower_player_one.change_point_value(self.players[0].lower_points)
        self.window.total_lower_player_two.change_point_value(self.players[1].lower_points)
        self.window.grand_total_player_one.change_point_value(self.players[0].lower_points)
        self.window.grand_total_player_two.change_point_value(self.players[1].lower_points)
