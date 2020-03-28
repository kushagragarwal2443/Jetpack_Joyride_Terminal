from colorama import Fore,Back,init
import os
import signal
import random

class Magnet:

    def __init__(self,xstart,ystart):
        self.__magnet=[]
        self.__xstart=xstart
        self.__ystart=ystart
        


    def definemagnet(self):
    
        with open("./background/magnet.txt") as magnet:
            for line in magnet:
                self.__magnet.append(line.strip("\n"))
    
    def createmagnet(self,matrix):

        while(True):
            count=0  
            for i in range(5):
                for j in range(14):
                    if(matrix[self.__xstart + i][self.__ystart +j] == " "):
                        count=count+1
            if(count==70):
                for i in range(5):
                    for j in range(14):
                        if(self.__magnet[i][j] =='*'):
                            matrix[self.__xstart + i][self.__ystart +j] = Back.CYAN + Fore.CYAN+self.__magnet[i][j]+ '\x1b[0m'
                        else:
                            matrix[self.__xstart + i][self.__ystart +j] = Back.BLACK + Fore.WHITE+self.__magnet[i][j]+ '\x1b[0m'
                xmag=self.__xstart+2
                ymag=self.__ystart+7
                return [xmag,ymag]
            else:
                self.__xstart=self.__xstart + random.randint(0,10)
                self.__xstart=self.__xstart - random.randint(0,10)
                if(self.__xstart <=7):
                    self.__xstart=7
                if(self.__xstart >=22 ):
                    self.__xstart=22
                self.__ystart=self.__ystart + 10 +  random.randint(0,9)