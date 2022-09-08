
import numpy as np


class Sudoku():

    def __init__(self,size):
        self.mat=np.ones((size*size,size*size), dtype="int32")

sud=Sudoku(3)
print(sud.mat)
