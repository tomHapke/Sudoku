import numpy as np
import pandas as pd
import csv
from .config.definitions import ROOT_DIR
from math import isqrt

class Sudoku():


    def __init__(self,size):
        self.numb=size
        self.len=size*size
        self.mat=np.zeros((self.len,self.len), dtype=int)
        self.pos=np.full((self.len,self.len),self.numb)
        self.probMat={}
        for index in range(self.numb):
            self.probMat[index]=np.zeros((self.len,self.len), dtype="float")

    def set(self,i,j,integer):
        #set Matrix on the specified field to integer
        self.mat[i,j]=integer
        #set Possibilty Matrix on the specified field to 1
        self.pos[i,j]=1
        #set every Probability Matrix on the specified field to 0.0
        for prob in self.probMat.values():
            prob[i,j]=0.0
        #set integer - Probability Matrix on the specified field to 1.0
        self.probMat[integer][i,j]=1.0

        #clear integer - Probability Matrix


    def load(path,name):
        absPath=ROOT_DIR+path+name
        matrix=pd.read_csv(absPath, dtype="integer").to_numpy
        sud=Sudoku(isqrt(matrix.shape[0]))
        sud.mat=matrix
        return sud



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
