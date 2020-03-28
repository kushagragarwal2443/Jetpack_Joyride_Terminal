from colorama import Fore,Back,init
import os
import signal
import random

class Beam:

    def __init__(self,xstart,ystart):
        self._xstart=xstart
        self._ystart=ystart
        self._xi=0
        self._yj=0

    def createBeams(self,matrix):
    
        count=0
        for i in range(self._xi):
            for j in range(self._yj):
                print(self._xstart, self._ystart)
                if(matrix[self._xstart + i][self._ystart +j] == " "):
                    count=count+1
        if(count==5):

            for i in range(self._xi):
                for j in range(self._yj):
                    matrix[self._xstart + i][self._ystart +j]=Back.RED + Fore.WHITE+ "*" + '\x1b[0m'
        
        
        self._xstart=self._xstart + random.randint(0,10)
        self._xstart=self._xstart - random.randint(0,10)
        if(self._xstart <=7):
            self._xstart=7
        if(self._xstart >=24 ):
            self._xstart=24
        self._ystart=self._ystart + 60 +  random.randint(0,9)
        return [self._xstart,self._ystart]


class BeamHori(Beam):
    def __init__(self,xstart,ystart):
        self._xstart=xstart
        self._ystart=ystart
        self._xi=1
        self._yj=5


class BeamVert(Beam):

    def __init__(self,xstart,ystart):
        self._xstart=xstart
        self._ystart=ystart
        self._xi=5
        self._yj=1

class BeamSla(Beam):

    def __init__(self,xstart,ystart):
        self._beamss=[]
        self._xstart=xstart
        self._ystart=ystart
        self._yj=0
        self._xi=0

    def createBeams(self,matrix):
        count=0
        for i in range(5):
            if(matrix[self._xstart + i][self._ystart +i] == " "):
                count=count+1
        if(count==5):
            for i in range(5):
                matrix[self._xstart + i][self._ystart +i]=Back.RED + Fore.WHITE+"*"+ '\x1b[0m'
        
        self._xstart=self._xstart + random.randint(0,10)
        self._xstart=self._xstart - random.randint(0,10)
        if(self._xstart <=7):
            self._xstart=7
        if(self._xstart >=24 ):
            self._xstart=24
        self._ystart=self._ystart + 60 +  random.randint(0,9)
        return [self._xstart,self._ystart]
