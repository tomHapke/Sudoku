import numpy as np
import pandas as pd
import csv
from math import isqrt
import os
from ..config.definitions import ROOT_DIR


class Sudoku():

    def __init__(self,size):
        self.size=size
        self.len=size*size
        self.mat=np.zeros((self.len,self.len), dtype=int)
        self.pos=np.zeros((self.len,self.len), dtype=int)
        self.noteMat={}
        for index in range(self.len):
            self.noteMat[index+1]=np.zeros((self.len,self.len), dtype="float")

    def setInitGamePlay(self,i,j,integer):
        #set Matrix on the specified field to integer
        self.mat[i,j]=integer
        #set Possibilty Matrix on the specified field to 1
        self.pos[i,j]=1
        #set integer - Note Matrix on the specified field to 1.0
        self.noteMat[integer][i,j]=1.0

    def setNoteGamePlay(self,i,j,integer):
        self.pos[i,j]+=1
        posibilities=self.pos[i,j]

        self.noteMat[integer][i,j]=1/posibilities

        for numb in range(1,self.len+1):
            if(self.noteMat[numb][i,j]!=0.0):
                self.noteMat[numb][i,j]=1/posibilities

    def deleteNoteGamePlay(self,i,j,integer):
        self.pos[i,j] -=1
        posibilities=self.pos[i,j]

        self.noteMat[integer][i,j]=0.0

        for numb in range(1,self.len+1):
            if(self.noteMat[numb][i,j]!=0.0):
                self.noteMat[numb][i,j]=1/posibilities

    def setGamePlay(self,i,j,integer):
        print("set "+str(integer))
        #set Matrix on the specified field to integer
        self.mat[i,j]=integer
        #set Possibilty Matrix on the specified field to 1
        self.pos[i,j]=1
        #set every Note Matrix on the specified field to 0.0
        for numb in range(1,self.len+1):
            self.noteMat[numb][i,j]=0.0
        #set integer - Note Matrix on the specified field to 1.0
        self.noteMat[integer][i,j]=1.0

        #clear integer - Note Matrix
        for index in range(self.len):
            if(index!=j):
                self.noteMat[integer][i,index]=0.0
        for index in range(self.len):
            if(index!=i):
                self.noteMat[integer][index,j]=0.0



    def store(self,path,name):
        absPath=ROOT_DIR+path+name
        try:
            with open(absPath, 'w') as my_new_csv_file:
                pass
        except:
            print("csv file could not be initialized")
        f = open(absPath, 'w')
        writer=csv.writer(f)
        for rowIndex in range(self.len):
            writer.writerow(self.mat[rowIndex])
        f.close()

    # returns if specified entry could be made accroding to the basic row-column-box-rule
    def isValidEntryBasicRule(self,i,j,integer):
        print("check basic row-column-box-rule")
        #row rule
        for r in range(self.len):
            if(self.mat[i,r]==integer):
                return False
        #column rule
        for r in range(self.len):
            if(self.mat[r,j]==integer):
                return False
        #box rule
        a=i//self.size
        b=j//self.size
        a=a*self.size
        b=b*self.size
        for r in range(self.size):
            for s in range(self.size):
                if(self.mat[a+r,b+s]==integer):
                    return False
        return True



def load(path,name):
    absPath=ROOT_DIR+path+name
    matrix=np.genfromtxt(absPath, delimiter=',',dtype="int")
    sud=Sudoku(isqrt(matrix.shape[0]))
    sud.mat=matrix
    return sud


#--------scripting
