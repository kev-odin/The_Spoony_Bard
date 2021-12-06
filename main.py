'''
Time used: 5 hours
xingguo
'''

# from adventurer import Adventurer
# from map import Map
# from dungeon import Dungeon
"""
Contains the main logic for playing the game
• Introduces the game describing what the game is about and how to play
• Creates a Dungeon Object and a Adventurer Object
• Obtains the name of the adventurer from the user
• Does the following repetitively:
    o Prints the current room (this is based on the Adventurer's current location)
    o Determines the Adventurer's options (Move, Use a Potion)
    o Continues this process until the Adventurer wins or dies
    o NOTE: Include a hidden menu option for testing that prints out the entire Dungeon -- specify what the menu option
        is in your documentation for the DungeonAdventure class
"""


class Main:

    # what to do with the init?
    # to create
    def __init__(self):
        pass


    def show_main_menu(self):
        # 1st menu:
            # show the title info(text), group info, basic instructions(h --help),(e -exit)
        # 2nd menu:
            # wsad-- u d l f
            # i for player current info health, pillar...
            # p for health pots
            # v for vision pots

        print("\nWelcome! Game logo/rules/info")  # read a text file to display the game logo
        help_or_continue = input("Please enter \'h\' for all commands of the game, or \'c\' for continue.")
        while True:
            if help_or_continue == 'h':
                print("complete commands of the game: \n"
                      "w: move up\n"
                      "s: move down\n"
                      "a: move left\n"
                      "d: move right"
                      "----to be continue----")
            if help_or_continue == 'c':
                break
        adventurer_name = input("Please enter a name for your adventurer: ")
        command = input("Please enter command: ")
        while True:
            command = input("")
            if command == 'h':
                self.display_basic_commands('h')
                continue
            elif command == 'e':
                break
            else:
                self.startGame()
            # handle exceptions(illegal inputs)
    def show_ingame_menu(self):
        pass

    def start_game(self):
        pass
        # create 1, 2, 3
        # get user command

    def move_adventurer(self):
        # adventurer interates with dun
        # if alive let the user to interacte if dead, exit
        # if adv at the exit? if adv has all the pillars?
        # add the traveled room to the list and display to the map
        pass

    def display_basic_commands(self):
        # print out ....   test it works correctly
        pass

    def display_adventurer_info(self):
        # to call __str__ function of ....?
        pass


if __name__ == "__main__": # when this file is run,
    main = Main()
    main.show_main_menu()







"""
____                                          
|    \  _ _  ___  ___  ___  ___  ___           
|  |  || | ||   || . || -_|| . ||   |          
|____/ |___||_|_||_  ||___||___||_|_|          
                 |___|                         
                                               
 _____    _                 _                  
|  _  | _| | _ _  ___  ___ | |_  _ _  ___  ___ 
|     || . || | || -_||   ||  _|| | ||  _|| -_|
|__|__||___| \_/ |___||_|_||_|  |___||_|  |___|  


Welcome to Dungeon Adventure! 

Your goal is to find all the four pillars of OOP and get to the exit safely. 

Each room of the dungeon will be randomly placed with the following items: 1⃣ Healing potion, 2⃣ Vision potion, 3⃣ Pit, 4⃣ OOP pillars, or nothing

If there are any items listed above 1⃣ -- 4⃣ in the room, you will automatically pick up the item(s) or take the damage.

For the Healing potion and Vision potion, you can choose to use them anytime you want. 

Beware that you have a limited amount of health pot, think before you jump to any room, and use the items wisely.

Good luck!!! 
"""