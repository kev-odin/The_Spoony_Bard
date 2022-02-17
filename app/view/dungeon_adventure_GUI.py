# checkout Kevin shared site https://www.pythontutorial.net/tkinter/
# checkout this site https://www.youtube.com/watch?v=tpwu5Zb64lQ
from tkinter import *

class dungeon_adventure_GUI:

    def __init__(self):
        self.root = Tk()  # create the root window
        self.root.resizable(width=False, height=False) # fixed size
        self.welcome_screen_frame = Frame(self.root)  # create a frame within that root window
        self.welcome_screen_canvas = Canvas(self.welcome_screen_frame,width=800, height=600, bg="black") # canvas within that frame
        self.welcome_window()
        self.welcome_screen_frame.pack()
        # self.welcome_screen_frame.forget
        self.root.mainloop()

    def create_new_game_window(self):
        '''
        Create a main window for the user to choose : new game, load game, quit game
        :return: None
        '''
        global game_difficulty  # global variable, look for details in def display_selected()
        global pop1  # to make it accessiable to other functions, otherwise tkinter won't work in our way
        pop1 = Toplevel(self.root)
        pop1.geometry("750x450")
        pop1.resizable(width=False, height=False)
        pop1.title("New Game")


        label1= Label(pop1, text="Select your game difficulty level")
        label1.pack()

        level_options = [
            "Easy",
            "Medium",
            "Hard",
            "Inhumane"
        ]
        level_options_description = {
            "Easy":"This is the easy mode.....",
            "Medium":"This is the medium mode.....",
            "Hard":"This is the hard mode.....",
            "Inhumane": "This is the Inhumane mode....."
        }

        clicked = StringVar()
        clicked.set(level_options[0]) # set the default greyed out level

        description_frame = Frame(pop1) # create a frame to hold label_frame1 and description_message

        def display_selected(selected):
            for widget in description_frame.winfo_children(): # Way to rewrite the label frame, looks for every child of frame
                widget.destroy() # delete
            selected = clicked.get()
            game_difficulty = selected # store the difficulty level in a variable

            label_frame1 = LabelFrame(description_frame, text=selected)
            label_frame1.pack()

            description_message = Message(label_frame1, text=level_options_description[selected], aspect=500)
            description_message.pack()


        option_menu1 = OptionMenu(pop1, clicked, *level_options, command=display_selected) # create a dropdown menu
        option_menu1.pack()

        lable2 = Label(pop1, text="Difficulty level descriptions:")
        lable2.pack()

        description_frame.pack() # pack it afterwards the line of "description_frame = Frame(pop1)"

        display_selected(clicked.get())

        btn2 = Button(pop1, text="Confirm New",command=lambda: self.get_adventurer_info(pop1)).place(relx=0.75,rely=0.9)

    def get_adventurer_info(self,pop1):
        '''
        To get user's preference of the hero name and the hero type
        :param pop1: the toplevel pop1 as the pop up window
        :return: None
        '''
        for widget in pop1.winfo_children():  # Way to rewrite the label frame, looks for every child of frame
            widget.destroy()  # delete

        label3 = Label(pop1, text="Choose your hero's name:").pack()
        hero_name = Entry(pop1).pack()

        label4 = Label(pop1, text="Choose your hero type:").pack()

        hero_options = [
            "Warrior",
            "Priest",
            "Thief"
        ]
        hero_options_description = {
            "Warrior": "This is the Warrior description.",
            "Priest": "This is the Priest description.",
            "Thief": "This is the Thief description."
        }
        clicked = StringVar()
        clicked.set(hero_options[0])  # set the default greyed out level

        hero_frame = Frame(pop1)

        def display_selected_hero(selected):
            for widget in hero_frame.winfo_children(): # Way to rewrite the label frame, looks for every child of frame
                widget.destroy() # delete
            selected = clicked.get()
            hero_type = selected # store the difficulty level in a variable

            label_frame2 = LabelFrame(hero_frame, text=selected)
            label_frame2.pack()

            hero_description = Message(label_frame2, text=hero_options_description[selected], aspect=500)
            hero_description.pack()

        option_menu2 = OptionMenu(pop1, clicked, *hero_options, command=display_selected_hero) # dropdown menu of hero types
        option_menu2.pack()

        hero_frame.pack() # we create the frame previously at line hero_frame = Frame(pop1), now we need pack()
        display_selected_hero(clicked.get()) # display the default hero type description.

        btn = Button(pop1, text="Confirm Hero", command=pop1.destroy).place(relx=0.75,rely=0.9) # here the pop1.destroy should be replaced by a function to send info the controller

    def load_existing_game_window(self):
        global pop2  # to make it accessiable to other functions, otherwise tkinter won't work in our way
        pop2 = Toplevel(self.root)
        pop2.geometry("750x450")
        pop2.resizable(width=False, height=False)
        label4 = Label(pop2, text="Choose the saved game:").pack()

        # option_menu3 = OptionMenu(pop2, clicked, *hero_options, command=display_selected_hero) # needs debug
        # option_menu3 = OptionMenu(pop2, "saved1","saved2")  # needs debug

        pop2.title("Load Game")

        btn3 = Button(pop2, text="Confirm Load", command = pop2.destroy).place(relx=0.75, rely=0.9)

    def welcome_window(self):

        canvas = self.welcome_screen_canvas

        new_game_btn = Button(canvas, text="New Game", command=self.create_new_game_window).place(relx=0.5,rely=0.5)
        load_game_btn = Button(canvas, text="Load Game", command=self.load_existing_game_window).place(relx=0.5, rely=0.6)
        quit_game_btn = Button(canvas, text="Quit Game", command=self.root.destroy).place(relx=0.5, rely=0.7)

        global img # to make it accessible to other functions, otherwise tkinter won't work in our way
        img = PhotoImage(file="welcome_bg.gif")
        canvas.create_image(0, 0, anchor=NW, image=img)
        canvas.pack()

if __name__ == "__main__":
    game = dungeon_adventure_GUI()


