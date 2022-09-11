import tkinter as tk
import time
from ..sudoku import sudoku as s
from functools import partial
import time
import os
import random as rd
from . import game_controller as gc
from time import sleep

from ..config.definitions import ROOT_DIR


LARGEFONT =("Verdana", 35)

global modes
modes=["Easy", "Medium", "Hard", "Emotional Damage"]
global maxMistakes
maxMistakes=4


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

    def setDifficultyButVisible(self):
        if(not self.difButtonsVisible):
            for i,mode in enumerate(modes):
                selectingCommandWithArg= partial(self.startGame, mode)
                self.difficultyButtons[mode]=tk.Button(self, text =mode, command=selectingCommandWithArg)
                #putting the difficulty button in its place
                self.difficultyButtons[mode].grid(row = 1, column = 2+i, padx = 10, pady = 10)
            self.difButtonsVisible=True
        else:
            self.difButtonsVisible=False
            for button in self.difficultyButtons.values():
                button.destroy()


    def startGame(self,mode):
        self.controller.show_frame(GamePage)
        self.controller.frames[GamePage].startGamePlay(mode)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller
        self.difButtonsVisible=False

        label = tk.Label(self, text ="Sudoku", font = LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row = 0, column = 1, padx = 10, pady = 10)

        button1 = tk.Button(self, text ="New game",
        command =self.setDifficultyButVisible)

        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 1, padx = 20, pady = 20)

        ## button to show frame 2 with text layout2
        button2 = tk.Button(self, text ="Stats",
        command = lambda : self.controller.show_frame(Page2))

        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 20, pady = 20)


        #difficulty buttons
        self.difficultyButtons={}


# second window frame page1
class GamePage(tk.Frame):

    def __init__(self, parent, controller):

        self.sudokuGridEntries=[]
        self.sudokuGridStringValues=[]
        self.sud=None
        tk.Frame.__init__(self, parent)
        self.controller=controller
        # button to show frame 2 with text
        # layout2
        buttonExit = tk.Button(self, text ="Exit",
                            command = self.exitGame,font=("Arial", 20,) )

        # putting the button in its place
        # by using grid
        buttonExit.grid(row = 1, column = 1, padx = 10, pady = 10)


        self.mistakeCounter=0
        self.mistakes=tk.Label(self, text ="Mistakes: 0", bg='#ff0000',font=("Arial", 20,))
        self.mistakes.grid(row = 2, column = 1, padx = 10, pady = 10)


        #explanation label

        explanation=tk.Label(self, text ="Fill in the numbers to confirm \n Take notes by writing e.g. \"(3,4,8)\".", font=("Arial", 10))
        explanation.grid(row = 3, column = 1, padx = 10, pady = 10)

    def setMistake(self,amount):
        self.mistakeCounter=amount
        self.mistakes["text"]="Mistakes: "+str(amount)

    def incrementMistake(self):
        self.mistakeCounter+=1
        self.setMistake(self.mistakeCounter)

    def startGamePlay(self, mode):
        self.sud=None
        self.sudokuGridEntries=[]
        self.sudokuGridStringValues=[]

        path="\\game\\games\\"+mode+"\\"
        gameFile=self.selectGame(os.listdir(ROOT_DIR +path))
        sud=s.load(path,gameFile)
        self.initSudokuGrid(sud)
        self.sud=sud

    def processInput(self,i,j,event):
        print("new State")
        self.sudokuGridEntries[i][j].config(state="readonly")
        if(self.sudokuGridStringValues[i][j].get()!=""):
            ans= gc.processPlayerInput(self.sud,self.sudokuGridStringValues[i][j].get(),i,j)

            print("Answer: "+str(ans))

            if(ans==-1):
                self.processMistake(i,j)

            if(not ans==1):
                if(self.sud.mat[i,j]!=0):
                    self.sudokuGridStringValues[i][j].set(self.sud.mat[i,j])
                else:
                    notes=[]
                    for numb in range(1,self.sud.len+1):
                        if(self.sud.noteMat[numb][i,j]!=0.0):
                            notes.append(numb)
                    if(len(notes)==0):
                        self.sudokuGridStringValues[i][j].set("")
                    else:
                        stringBuilder="("
                        for index,numb in enumerate(note):
                            if(index==len(notes)-1):
                                stringBuilder=stringBuilder+str(numb)+")"
                                break
                            stringBuilder=stringBuilder+str(numb)+","
                        self.sudokuGridStringValues[i][j].set(stringBuilder)
        self.sudokuGridEntries[i][j].config(state="normal")

    def processMistake(self,i,j):
        #for step in range(3):
            #self.controller.after(500,self.sudokuGridStringValues[i][j].set("mistake!"))
            #self.controller.after(500,self.sudokuGridStringValues[i][j].set(" "))
        self.incrementMistake()

        if(self.mistakeCounter>=maxMistakes):
            #for a in range(self.sud.len):
            #    for b in range(self.sud.len):
            #        self.sudokuGridStringValues[i][j].set("TOO MANY MISTAKES!")
            self.mistakes["text"]="TOO MANY MISTAKES!"
            self.exitGame()

    def initSudokuGrid(self,sud):
        for i in range(sud.len):
            rowEntry=[]
            rowStringVar=[]
            for j in range(sud.len):
                stringVar=tk.StringVar()
                if(sud.mat[i,j]!=0):
                    stringVar.set(sud.mat[i,j])
                rowStringVar.append(stringVar)
                partialProcessInput=partial(self.processInput, i,j)
                entry=tk.Entry(self,textvariable=stringVar, width=10)
                entry.bind("<FocusOut>", partialProcessInput)
                rowEntry.append(entry)
                entry.grid(row = 1+i, column = 2+j, padx = 10, pady = 10)
            self.sudokuGridEntries.append(rowEntry)
            self.sudokuGridStringValues.append(rowStringVar)

    def selectGame(self,list):
        return list[rd.randrange(len(list))]

    def exitGame(self):
        print("exit game")
        if(self.controller.frames[StartPage].difButtonsVisible):
            self.controller.frames[StartPage].setDifficultyButVisible()
        self.controller.show_frame(StartPage)
        self.setMistake(0)

        #delete Grid
        for i in range(len(self.sudokuGridEntries)):
            for j in range(len(self.sudokuGridEntries[i])):
                self.sudokuGridEntries[i][j].destroy()

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
