from colorama import Fore,Back,init
import os
import signal
import random

class Coins:

    def __init__(self,xstart,ystart):
        self.__coins=[]
        self.__xstart=xstart
        self.__ystart=ystart


    def defineCoins(self):
    
        with open("./background/coins.txt") as coins:
            for line in coins:
                self.__coins.append(line.strip("\n"))
    
    def createCoins(self,matrix):

        count=0  
        for i in range(2):
            for j in range(5):
                if(matrix[self.__xstart + i][self.__ystart +j] == " "):
                    count=count+1
        if(count==10):
            for i in range(2):
                for j in range(5):
                    matrix[self.__xstart + i][self.__ystart +j]=Fore.YELLOW +self.__coins[i][j]+ '\x1b[0m'

        self.__xstart=self.__xstart + random.randint(0,10)
        self.__xstart=self.__xstart - random.randint(0,10)
        if(self.__xstart <=7):
            self.__xstart=7
        if(self.__xstart >=25 ):
            self.__xstart=25
        self.__ystart=self.__ystart + 60 +  random.randint(0,9)

        return [self.__xstart,self.__ystart]
