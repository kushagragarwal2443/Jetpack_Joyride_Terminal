import os
import time
import random
import signal
from colorama import Fore, Back, init

class Dragonball:

    def __init__(self):

        self.__ball=[{'x':0,'y':0,'enable':0} for k in range(100)]
        self.__dragonball="*"

    def getball(self):
        return self.__ball
    def setball(self,balls):
        self.__ball=balls

    def addballtoboard(self,matrix):
        for i in range(100):
            if(self.__ball[i]["enable"]==1):

                matrix[self.__ball[i]["x"]][self.__ball[i]["y"]]=Fore.RED + self.__dragonball + '\x1b[0m'
        return matrix

    def removeballfromboard(self,matrix):
        for i in range(100):
            if(self.__ball[i]["enable"]==1):

                matrix[self.__ball[i]["x"]][self.__ball[i]["y"]]=" "
        return matrix

    def timeincreased(self):
        for i in range(100):
            if(self.__ball[i]["enable"]==1):
                self.__ball[i]["y"]=self.__ball[i]["y"]-2
            
            if(self.__ball[i]["y"]<=680):
                self.__ball[i]["enable"]=0


    def firebullets(self,iter,xstart,ystart):

        self.__ball[iter]["x"]=xstart
        self.__ball[iter]["y"]=ystart
        self.__ball[iter]["ystart"]=ystart
        self.__ball[iter]["enable"]=1

    
        