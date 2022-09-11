from ...sudoku import sudoku as s
from random import randrange



size = 3
mode = "Easy"
id="2"

sud=s.Sudoku(size)

len=sud.len

#set randon ints from 1 to sud.numb
for i in range(len):
    for j in range(len):
        p =randrange(2)   # leave a bunch at 0
        if(p==0):
            s.Sudoku.setInitGamePlay(sud,i,j,randrange(sud.len)+1)



sud.store("\\game\\games\\"+mode+"\\","randomSudoku"+str(id)+".csv")
