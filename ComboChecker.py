from Dice import Dice
from Indices import Indices
from Player import Player

FULL_HOUSE_POINTS: int = 25
SMALL_STRAIGHT_POINTS: int = 30
LARGE_STRAIGHT_POINTS: int = 40
YAHTZEE_POINTS: int = 50


class ComboChecker:
    def __init__(self, _dice_list: list[Dice], _current_player: Player):
        self.dice_list: list[Dice] = _dice_list
        self.dice_roll_nums: list[int] = self.num_check()
        self.current_player = _current_player

    def num_check(self):
        """Checks number of aces, twos, threes, four, fives, and sixes, and stores them as a list"""
        aces = 0
        twos = 0
        threes = 0
        fours = 0
        fives = 0
        sixes = 0
        for die in self.dice_list:
            match die.get_number():
                case 1:
                    aces += 1
                case 2:
                    twos += 1
                case 3:
                    threes += 1
                case 4:
                    fours += 1
                case 5:
                    fives += 1
                case 6:
                    sixes += 1
                case _:
                    raise ValueError("Incorrect dice value!")
        self.dice_roll_nums = [aces, twos, threes, fours, fives, sixes]

    def check(self) -> dict[str, int]:
        # Declare dictionary and points
        points_dict: dict[str, int] = {}
        points: int

        # Check aces
        points = self.aces()
        points_dict.update({"Aces": points})
        # Check twos
        points = self.twos()
        points_dict.update({"Twos": points})
        # Check threes
        points = self.threes()
        points_dict.update({"Threes": points})
        # Check fours
        points = self.fours()
        points_dict.update({"Fours": points})
        # Check fives
        points = self.fives()
        points_dict.update({"Fives": points})
        # Check sixes
        points = self.sixes()
        points_dict.update({"Sixes": points})
        # Check for threes of a kind
        points = self.three_of_a_kind()
        points_dict.update({"3 of a Kind": points})
        # Check for fours of a kind
        points = self.four_of_a_kind()
        points_dict.update({"4 of a Kind": points})
        # Check for full house
        points = self.full_house()
        points_dict.update({"Full House": points})
        # Check for small straight
        points = self.small_straight()
        points_dict.update({"Small Straight": points})
        # Check for large straight
        points = self.large_straight()
        points_dict.update({"Large Straight": points})
        # Check for yahtzee
        points = self.yahtzee()
        points_dict.update({"Yahtzee": points})
        # Check for chance
        points = self.chance()
        points_dict.update({"Chance": points})
        # Check for yahtzee bonus
        points = self.yahtzee_bonus()
        points_dict.update({"Yahtzee Bonus": points})

        # Return array
        return points_dict

    def aces(self) -> int:
        return self.dice_roll_nums[Indices.ACE_INDEX.value]

    def twos(self) -> int:
        return self.dice_roll_nums[Indices.TWOS_INDEX.value] * 2

    def threes(self) -> int:
        return self.dice_roll_nums[Indices.THREES_INDEX.value] * 3

    def fours(self) -> int:
        return self.dice_roll_nums[Indices.FOURS_INDEX.value] * 4

    def fives(self) -> int:
        return self.dice_roll_nums[Indices.FIVES_INDEX.value] * 5

    def sixes(self) -> int:
        return self.dice_roll_nums[Indices.SIXES_INDEX.value] * 6

    def three_of_a_kind(self) -> int:
        value: int = 0
        # Checks if any combinations of three exist
        for x in range(len(self.dice_roll_nums)):
            if self.dice_roll_nums[x] == 3:
                # Add the faces of each dice roll
                for y in range(len(self.dice_roll_nums)):
                    value += self.dice_roll_nums[y] * (y + 1)
        return value

    def four_of_a_kind(self) -> int:
        value: int = 0
        # Checks if any combinations of four exist
        for x in range(len(self.dice_roll_nums)):
            if self.dice_roll_nums[x] == 4:
                # Add the faces of each dice roll
                for y in range(len(self.dice_roll_nums)):
                    value += self.dice_roll_nums[y] * (y + 1)
        return value

    def full_house(self) -> int:
        comb2: bool = False
        comb3: bool = False
        # Checks if a combination of 3 and a combination of 2 exist
        for x in range(len(self.dice_roll_nums)):
            if self.dice_roll_nums[x] == 2:
                comb2 = True
            elif self.dice_roll_nums[x] == 3:
                comb3 = True
        # Checks if both combinations exist
        if comb2 and comb3:
            return FULL_HOUSE_POINTS
        else:
            return 0

    def small_straight(self) -> int:
        # Checks if there is a 3 or a 4
        if self.dice_roll_nums[Indices.THREES_INDEX.value] > 0 and self.dice_roll_nums[Indices.FOURS_INDEX.value] > 0:
            # Checks if there are other pairs of numbers that complete a small straight
            if self.dice_roll_nums[Indices.ACE_INDEX.value] > 0 and self.dice_roll_nums[Indices.TWOS_INDEX.value] > 0:
                return SMALL_STRAIGHT_POINTS
            elif self.dice_roll_nums[Indices.TWOS_INDEX.value] > 0 and self.dice_roll_nums[Indices.FIVES_INDEX.value] > 0:
                return SMALL_STRAIGHT_POINTS
            elif self.dice_roll_nums[Indices.FIVES_INDEX.value] > 0 and self.dice_roll_nums[Indices.SIXES_INDEX.value] > 0:
                return SMALL_STRAIGHT_POINTS
            else:
                return 0
        return 0

    def large_straight(self) -> int:
        # Test if it matches any large-straight sequences
        if self.dice_roll_nums == [1, 1, 1, 1, 1, 0] or self.dice_roll_nums == [0, 1, 1, 1, 1, 1]:
            return LARGE_STRAIGHT_POINTS
        else:
            return 0

    def yahtzee(self) -> int:
        # Check if there is a combination of 5 numbers
        for x in range(len(self.dice_roll_nums)):
            if self.dice_roll_nums[x] == 5:
                return YAHTZEE_POINTS
        return 0

    def chance(self):
        value: int = 0
        # Add the faces of each dice roll
        for x in range(len(self.dice_roll_nums)):
            value += self.dice_roll_nums[x] * (x + 1)
        return value

    def yahtzee_bonus(self) -> int:
        value: int = 0
        if self.current_player.has_yahtzee:
            value = self.yahtzee()
        return value

    def bonus(self) -> int:
        if self.current_player.upper_points >= 63:
            return 35
        else:
            return 0

    def generate_table_dict(self) -> dict[str, int]:
        self.num_check()
        table_dict: dict[str, int] = {}
        roll_dict: dict[str, int] = self.check()
        for combo in roll_dict.keys():
            if roll_dict[combo] != 0 and self.current_player.combo_dict[combo]:
                table_dict.update({combo: roll_dict[combo]})
        return table_dict
