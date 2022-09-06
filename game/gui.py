import tkinter as tk
import time

LARGEFONT =("Verdana", 35)

class game(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self,*args,**kwargs)

        container = tk.Frame(self)
        container.pack(side = "top", fill ="both", expand= True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames ={}

        for F in (StartPage, GamePage, StatsPage):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky ="nsew")

        self.show_frame(StartPage)


    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def selectDifficulty(frame):
        button1 = tk.Button(frame, text ="Easy")

        button2 = tk.Button(frame, text ="Middle")

        button3 = tk.Button(frame, text ="Hard")

        button4 = tk.Button(frame, text ="Emotional Damage")

        #putting the difficulty button in its place

        button1.grid(row = 1, column = 2, padx = 10, pady = 10)
        button2.grid(row = 1, column = 3, padx = 10, pady = 10)
        button3.grid(row = 1, column = 4, padx = 10, pady = 10)
        button4.grid(row = 1, column = 5, padx = 10, pady = 10)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of frame Layout 2
        label = tk.Label(self, text ="Sudoku", font = LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row = 0, column = 4, padx = 10, pady = 10)

        button1 = tk.Button(self, text ="New game",
        command = lambda : selectDifficulty(self))

        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 1, padx = 20, pady = 20)

        ## button to show frame 2 with text layout2
        button2 = tk.Button(self, text ="Stats",
        command = lambda : controller.show_frame(Page2))

        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 20, pady = 20)





# second window frame page1
class GamePage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text ="Page 1", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)

        # button to show frame 2 with text
        # layout2
        button1 = tk.Button(self, text ="StartPage",
                            command = lambda : controller.show_frame(StartPage))

        # putting the button in its place
        # by using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)

        # button to show frame 2 with text
        # layout2
        button2 = tk.Button(self, text ="Page 2",
                            command = lambda : controller.show_frame(Page2))

        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)

class StatsPage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text ="Page 1", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)

        # button to show frame 2 with text
        # layout2
        button1 = tk.Button(self, text ="StartPage",
                            command = lambda : controller.show_frame(StartPage))

        # putting the button in its place
        # by using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)

        # button to show frame 2 with text
        # layout2
        button2 = tk.Button(self, text ="Page 2",
                            command = lambda : controller.show_frame(Page2))

        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)

game=game()
game.mainloop()
