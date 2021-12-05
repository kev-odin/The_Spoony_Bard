# Kevin's Time Tracker: 2.5 hours
import random

class Adventurer:
    """Adventurer that traverses through the maze. Picks up potions, falls into pits, and
    must complete the maze with all OOP pillars (APIE) collected to win.
    """
    # TODO:
    # 1) Determine how to manage potion inventory
    # 2) How does adventurer check the state of the room?
    # 3) Auto pick up potion in a room
    # 4) Working observer pattern with adventurer and potion factory?
    # 5) Random hitpoint generator <-
    # 6) Write tests


    def __init__(self, name = None, challenge = 'easy'):
        self.__name = name
        self.__dev_powers = False
        self.__hitpoints = 75
        self.__health_pots = 0
        self.__vision_pots = 0
        self.__pillars = {
            'A' : False,
            'P' : False,
            'I' : False,
            'E' : False
        }

        self._create_adventurer(name, challenge)

    def is_alive(self):
        return self.hitpoints > 0

    def _create_adventurer(self, name, challenge):
        """Helper method for character creation. Difficulty and name are checked,
        based on those values, create an adventurer with modified base values.

        :param name: str if found in cheat_code dictionary, modification applied to adventurer
        :param challenge: str sets to following challenge level 'easy' 3x, 'medium' 2x, 'hard' 1x, 'inhumane' 0x
        """
        difficulty = {
            'easy' : 3,
            'medium' : 2,
            'hard' : 1,
            'inhumane' : 0
        }

        cheat_codes = {
            'tom' : 'no health lost',
            'kevin' : 'unlimited potions'
        }

        if name in cheat_codes:
            self.dev_powers = True

        hp_mod = 1

        if challenge in difficulty:
            hp_mod = difficulty[challenge]
            self.hitpoints += hp_mod * random.randint(0, 10)

        self.health_pots = 0
        self.vision_pots = 0

    def __str__(self):
        player_stats = f'Name: {self.name}\nHP: {self.hitpoints}\nHealth potions: {self.health_pots} \
                        \nVision potions: {self.vision_pots}\nPillars collected: {self.__pillars}'
        return player_stats

    @property
    def name(self):
        """Getter for name property

        :return: name of adventurer
        :rtype: str
        """
        return self.__name

    @name.setter
    def name(self, value):
        """Setter for the name property

        :param value: name provided by user
        :type value: str
        """
        if isinstance(value, str):
            self.__name = value

    @property
    def dev_powers(self):
        """Getter for the dev_powers property

        :return: status if cheat codes are enabled
        :rtype: bool
        """
        return self.__dev_powers

    @dev_powers.setter
    def dev_powers(self, value):
        """Setter for the dev_powers property

        :param value: boolean if cheat codes are enabled
        """
        if isinstance(value, bool):
            self.__dev_powers = value

    @property
    def hitpoints(self):
        """Getter for hitpoints property

        :return: health remaining of adventurer
        :rtype: int
        """
        return self.__hitpoints

    @hitpoints.setter
    def hitpoints(self, value):
        """Setter for the hitpoints property

        :param value: damage incurred from pits
        :type value: int
        """
        if isinstance(value, int):
            self.__hitpoints = value

    @property
    def health_pots(self):
        """Getter for health potion property

        :return: number of health potions for adventurer
        :rtype: int
        """
        return self.__health_pots

    @health_pots.setter
    def health_pots(self, value):
        """Setter for the health potion property

        :param value: number of potions found in the room
        :type value: int
        """
        if isinstance(value, int):
            self.__health_pots = value

    @property
    def vision_pots(self):
        """Getter for vision pots property

        :return: number of vision potions for adventurer
        :rtype: int
        """
        return self.__vision_pots

    @vision_pots.setter
    def vision_pots(self, value):
        """Setter for the health pots property

        :param value: number of potions found in the room
        :type value: int
        """
        if isinstance(value, int):
            self.__vision_pots = value
