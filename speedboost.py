from colorama import Fore,Back,init
import os
import signal
import random

class Speed:

    def __init__(self,xstart,ystart):
        self.__speed=[]
        self.__xstart=xstart
        self.__ystart=ystart
        


    def definespeed(self):
    
        with open("./background/speedboost.txt") as speed:
            for line in speed:
                self.__speed.append(line.strip("\n"))
    
    def createspeed(self,matrix):

        while(True):
            count=0  
            for i in range(3):
                for j in range(9):
                    if(matrix[self.__xstart + i][self.__ystart +j] == " "):
                        count=count+1
            if(count==27):
                for i in range(3):
                    for j in range(9):
                        if(self.__speed[i][j] =='@'):
                            matrix[self.__xstart + i][self.__ystart +j] = Back.MAGENTA + Fore.MAGENTA+self.__speed[i][j]+ '\x1b[0m'
                        else:
                            matrix[self.__xstart + i][self.__ystart +j] = Back.BLACK + Fore.WHITE+self.__speed[i][j]+ '\x1b[0m'
                break
            else:
                self.__xstart=self.__xstart + random.randint(0,10)
                self.__xstart=self.__xstart - random.randint(0,10)
                if(self.__xstart <=7):
                    self.__xstart=7
                if(self.__xstart >=22 ):
                    self.__xstart=22
                self.__ystart=self.__ystart + 30 +  random.randint(0,9)