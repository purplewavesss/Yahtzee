import random
from PyQt5 import QtWidgets
import Dice
import MainWindow
import Player
import PointItem
from ComboChecker import ComboChecker


def table_dict_display(point_item: PointItem, points: int):
    point_item.set_status("potential")
    point_item.setText(str(points))


def gen_win_box(text: str):
    win_message_box = QtWidgets.QMessageBox()
    win_message_box.setWindowTitle("Winner")
    win_message_box.setIcon(QtWidgets.QMessageBox.NoIcon)
    win_message_box.setText(text)
    win_message_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
    win_message_box.exec()

# Encapsulates the main game functionalities.

class Game:
    def __init__(self, _window: MainWindow, _players: list[Player]):
        self.window = _window
        self.players = _players
        self.__current_player: Player = self.players[0]
        self.dice_list: list[Dice] = [self.window.dice_1, self.window.dice_2, self.window.dice_3, self.window.dice_4,
                                      self.window.dice_5]
        self.combo_checker: ComboChecker = ComboChecker(self.dice_list, self.__current_player)
        self.table_dict: dict[str, int] = {}
        self.winner: Player = None
        self.tie: bool = False
        for die in self.dice_list:
            die.setHidden(True)

    def roll(self):
        # Switch player
        if self.__current_player.round_finished:
            if self.__current_player.player_num == 1:
                self.set_current_player(self.players[1])
            else:
                self.set_current_player(self.players[0])
            self.__current_player.roll_num = 0
            self.__current_player.can_click = True

        if self.__current_player.can_click:
            # Rename button label
            self.window.roll_button.setText("Roll!")

            # Increment roll number
            self.__current_player.roll_num += 1

            # Clear table
            self.__current_player.clear_potential_point_items()

            # Roll dice
            for die in self.dice_list:
                if die.first_round:
                    die.first_round = False
                if not die.get_locked():
                    die.set_number(random.randint(1, 6))
                die.setHidden(False)

            # Generate dictionary of possible point item table values
            table_dict = self.combo_checker.generate_table_dict()

            # Check if table dictionary has a length of zero
            if len(table_dict) == 0:
                table_dict = self.combo_checker.generate_zero_dict(self.__current_player.combo_dict)
                if len(table_dict) == 0:
                    self.game_end(True)

            # Display table items
            self.display_items(table_dict)

            if self.__current_player.roll_num == 3:
                self.__current_player.can_click = False

        else:
            self.window.roll_button.setText("Can't roll!")

    def set_current_player(self, _current_player: Player):
        self.__current_player = _current_player
        self.combo_checker.current_player = self.__current_player
        self.window.player_label.set_current_player(self.__current_player)

    def display_items(self, table_dict: [str, int]):
        for combo in table_dict.keys():
            if self.__current_player.player_num == 1:
                # Switch statement to fill combos for Player 1
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
                # Switch statement to fill combos for Player 2
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

        # Update upper bonus and upper/lower scores
        if self.__current_player.has_bonus:
            if self.__current_player.player_num == 1:
                self.window.total_player_one.set_point_value(self.__current_player.upper_points + 35)
                self.window.total_upper_player_one.set_point_value(self.__current_player.upper_points + 35)
            else:
                self.window.total_player_two.set_point_value(self.__current_player.upper_points + 35)
                self.window.total_upper_player_two.set_point_value(self.__current_player.upper_points + 35)
        else:
            self.window.total_upper_player_one.set_point_value(self.players[0].upper_points)
            self.window.total_upper_player_two.set_point_value(self.players[1].upper_points)

        # Update totals
        self.window.total_score_player_one.set_point_value(self.players[0].upper_points)
        self.window.total_score_player_two.set_point_value(self.players[1].upper_points)
        self.window.total_lower_player_one.set_point_value(self.players[0].lower_points)
        self.window.total_lower_player_two.set_point_value(self.players[1].lower_points)
        self.window.grand_total_player_one.set_point_value(self.players[0].upper_points +
                                                           self.players[0].lower_points)
        self.window.grand_total_player_two.set_point_value(self.players[1].upper_points +
                                                           self.players[1].lower_points)

    def game_end(self, show_winner: bool):
        # Clear point items
        for player in self.players:
            player.erase_point_items()

        # Reset roll button
        self.window.roll_button.setText("Start Game")

        # Hide dice
        for die in self.dice_list:
            die.setHidden(True)

        # Change current player to Player 1
        self.set_current_player(self.players[0])

        if show_winner:
            # Check which player won
            if self.window.grand_total_player_one.get_point_value() > self.window.grand_total_player_two.get_point_value():
                self.winner = self.players[0]
            elif self.window.grand_total_player_one.get_point_value() < self.window.grand_total_player_two.get_point_value():
                self.winner = self.players[1]
            else:
                self.tie = True

            # Display tie message box
            if self.tie:
                gen_win_box("It was a tie!")

            # Display winner message box
            else:
                gen_win_box(f'Player {self.winner.player_num} won with {self.winner.total_points} points!')
