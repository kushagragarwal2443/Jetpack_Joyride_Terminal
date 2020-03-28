import random
import signal
import os
from colorama import Fore, Back, init

class Dragon:

    def __init__(self,xstart,ystart):
        self.__dragonxcod=xstart+7
        self.__dragonycod=ystart+22
        self.__dragon=[]

    

    def getDragcood(self):
        return [self.__dragonxcod, self.__dragonycod]
    def setDragcood(self,xcod,ycod):
        self.__dragonycod=ycod
        self.__dragonxcod=xcod

    def createDragon(self):
        with open("./background/dragons.txt") as dragon:
            for line in dragon:
                self.__dragon.append(line.strip("\n"))
    

    def printDragon(self,matrix):
        for i in range(14):
            for j in range(44):
                if(self.__dragon[i][j]=='D' or self.__dragon[i][j]=='_' ):
                    matrix[self.__dragonxcod - 7 + i][self.__dragonycod -22 + j]=Fore.RED + self.__dragon[i][j] +'\x1b[0m'
                elif(self.__dragon[i][j]=='.' or self.__dragon[i][j]==',' or self.__dragon[i][j]=="X"):
                    matrix[self.__dragonxcod - 7 + i][self.__dragonycod -22 + j]=Fore.YELLOW + self.__dragon[i][j] +'\x1b[0m'
                elif(self.__dragon[i][j]=='\\' or self.__dragon[i][j]=="=" ):
                    matrix[self.__dragonxcod - 7 + i][self.__dragonycod -22 + j]=Fore.BLUE + self.__dragon[i][j] +'\x1b[0m'
                else:
                    matrix[self.__dragonxcod - 7 + i][self.__dragonycod -22 + j]=Fore.GREEN+ self.__dragon[i][j] +'\x1b[0m'

    def delDragon(self,matrix):
        for i in range(14):
            for j in range(44):
                matrix[self.__dragonxcod - 7 + i][self.__dragonycod -22 + j]=" "




    def Dragmove(self,x):

        #x,y are the coordinates of the mando at that time
        dragx=self.__dragonxcod
        if(dragx-x>0):
            dragx=dragx-1
        elif(dragx-x <0):
            dragx=dragx+1

        if(dragx + 7 >=27):
            dragx=20
        elif(dragx-7 <=2):
            dragx=9
        
        self.__dragonxcod=dragx   
