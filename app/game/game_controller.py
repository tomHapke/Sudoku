from ..sudoku import sudoku as s

#returns 1, if valid, 0, if invalid, -1, if mistake
def processPlayerInput(sudoku,sValue,i,j):
    if(sudoku.mat[i,j]!=0):
        return 0
    for numb in range(sudoku.len):
        if(sValue==str(numb+1)):
            if(s.Sudoku.isValidEntryBasicRule(sudoku,i,j,numb+1)):
                s.Sudoku.setGamePlay(sudoku,i,j,numb+1)
                return 1
            else:
                return -1
    notes=[]
    for index in range(len(sValue)):
        if(index==0 and sValue[0]!="("):
            print("no bracket at the beginning")
            return 0
        elif(index==len(sValue)-1 and sValue[0]!=")"):
            print("no bracket at the end")
            return 0
        elif(sValue[index]==","):
            index+=1
        elif(sValue[index].isdigit()):
            temp=index
            while(sValue[temp].isdigit()):
                temp+=1
            print(sValue[index:temp])
            nodes.append(int(sValue[index:temp]))
            index=temp
        else:
            print("wrong syntax in note input")
            return 0

    if(len(notes)==0):
        print("empty bracket")
        return 0

    numbs =range(1,sudoku.len+1)
    for nodeInt in notes:
        if(sudoku.noteMat[nodeInt][i,j]==0.0):
            s.Sudoku.setNoteGamePlay(sudoku,i,j,nodeInt)
        numbs.pop(nodeInt)

    #delete notes that are not there anymore
    for nodeInt in numbs:
        if(sudoku.noteMat[nodeInt][i,j]!=0.0):
            s.Sudoku.deleteNoteGamePlay(sudoku,i,j,nodeInt)
    return 1
