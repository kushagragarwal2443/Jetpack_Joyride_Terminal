import random
import time
import signal
import os
from colorama import Fore, Back, init

class Bullets:

    def __init__(self):

        self.__bullets= [{'x':0,'y':0,'enable':0,'ystart':0} for k in range(100)]
        self.__usedbullets=0
        self.__bullet="0"
        self.__dragonlife=5
        self.__dragonscore=0

    def getbullet(self):
        return self.__bullets
    def setbullet(self,bullets):
        self.__bullets=bullets

    def getdragonlife(self):
        return self.__dragonlife
    def getdragonscore(self):
        return self.__dragonscore


    def addbullettoboard(self,matrix):
        for i in range(100):
            if(self.__bullets[i]["enable"]==1):

                matrix[self.__bullets[i]["x"]][self.__bullets[i]["y"]]=self.__bullet
        return matrix

    def removebulletfromboard(self,matrix):
        for i in range(100):
            if(self.__bullets[i]["enable"]==1):

                matrix[self.__bullets[i]["x"]][self.__bullets[i]["y"]]=" "
        return matrix

    def timeincreased(self):
        for i in range(100):
            if(self.__bullets[i]["enable"]==1):
                self.__bullets[i]["y"]=self.__bullets[i]["y"]+2
            
            if(self.__bullets[i]["y"]>=798):
                self.__bullets[i]["enable"]=0


    def firebullets(self,iter,xstart,ystart):

        self.__bullets[iter]["x"]=xstart
        self.__bullets[iter]["y"]=ystart
        self.__bullets[iter]["ystart"]=ystart
        self.__bullets[iter]["enable"]=1
        self.__usedbullets=self.__usedbullets+1

    def checkbullcoll(self,matrix):

        for i in range(self.__usedbullets):
            if(self.__bullets[i]["enable"] == 1):
                xcod=self.__bullets[i]["x"]

                ycod=self.__bullets[i]["y"]

                if(matrix[xcod][ycod]==Back.RED + Fore.WHITE+ "*" +'\x1b[0m' or matrix[xcod][ycod]==Back.CYAN + Fore.CYAN+ "*" +'\x1b[0m' or matrix[xcod][ycod]==Fore.YELLOW +'$'+ '\x1b[0m' or matrix[xcod][ycod]==Back.MAGENTA + Fore.MAGENTA+'@'+ '\x1b[0m'):
                    matrix[xcod][ycod]=" "
                    self.__bullets[i]["enable"]=0
                elif(matrix[xcod][ycod+1]==Back.RED + Fore.WHITE+ "*" +'\x1b[0m' or matrix[xcod][ycod+1]==Back.CYAN + Fore.CYAN+ "*" +'\x1b[0m' or matrix[xcod][ycod+1]==Fore.YELLOW +'$'+ '\x1b[0m' or matrix[xcod][ycod+1]==Back.MAGENTA + Fore.MAGENTA+'@'+ '\x1b[0m'):
                    matrix[xcod][ycod+1]=" "
                    self.__bullets[i]["enable"]=0
                
                elif(matrix[xcod][ycod]==Fore.YELLOW +"X"+'\x1b[0m'):
                    self.__dragonlife=self.__dragonlife-1
                    self.__dragonscore=self.__dragonscore+5
                    self.__bullets[i]["enable"]=0
                elif(matrix[xcod][ycod+1]==Fore.YELLOW +"X"+'\x1b[0m'):
                    self.__dragonlife=self.__dragonlife-1
                    self.__dragonscore=self.__dragonscore+5
                    self.__bullets[i]["enable"]=0
                    
        return matrix

    def expirebullet(self):

        for i in range(100):
            if(self.__bullets[i]["y"] - self.__bullets[i]["ystart"] >= 120):
                self.__bullets[i]["enable"]=0

        