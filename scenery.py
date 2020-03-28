import os
import random
from colorama import init,Fore,Back

from coins import Coins
from zappers import Beam,BeamHori,BeamSla,BeamVert
from magnet import Magnet
from speedboost import Speed




class Scenery:

    def __init__(self):

        self.__cloud=[]
        self.__sky=[]
        self.__ground=[]
        self.__speed=[]
        self.__xmag=0
        self.__ymag=0


    def getMagCood(self):
        return [self.__xmag,self.__ymag]

    def setMagCood(self,xmag,ymag):
        self.__xmag=xmag
        self.__ymag=ymag

    def createGround(self,matrix):

        for i in range(800):
            #matrix[29][i]=random.randint(0,9)
            #matrix[28][i]=random.randint(0,9)
            matrix[29][i]= Fore.WHITE+"%"+'\x1b[0m'
            matrix[28][i]= Fore.GREEN + Back.GREEN+"%"+'\x1b[0m'
            

    def createSky(self, matrix):
        for i in range(800):
            #matrix[0][i]=random.randint(0,9)
            #matrix[1][i]=random.randint(0,9)
            matrix[0][i]= Fore.WHITE+"%" +'\x1b[0m'
            matrix[1][i]= Fore.MAGENTA+Back.MAGENTA+"%" + '\x1b[0m'


  
    def createClouds(self,matrix,xstart,ystart):

        with open("./background/cloud.txt") as cloud:
            for line in cloud:
                self.__cloud.append(line.strip("\n"))

        #the clouds stop at column number 500(so that enemy gets time and no interference)

        while(True):
            for i in range(5):
                for j in range(16):
                    matrix[xstart +i][ystart + j]= self.__cloud[i][j]+ '\x1b[0m'


            xstart=xstart + random.randint(0,2)
            xstart=xstart - random.randint(0,2)
            ystart=ystart + 60 +  random.randint(0,9)

            if(xstart<=3):
                xstart=3
            if(xstart>=8):
                xstart=5
            if( ystart >=664):
                break


    def createCoins(self,matrix,xstart,ystart):
    
        while(True):
            obj_coin=Coins(xstart,ystart)
            obj_coin.defineCoins()
            [xstart,ystart]=obj_coin.createCoins(matrix)
            if(ystart>=675):
                break
            

    def createBeamsh(self,matrix,xstart,ystart):
    
        while(True):
            obj_beamh=BeamHori(xstart,ystart)
            [xstart,ystart]=obj_beamh.createBeams(matrix)
            if(ystart>=675):
                break


    def createBeamsv(self,matrix,xstart,ystart):
    
        while(True):
            obj_beamv=BeamVert(xstart,ystart)
            [xstart,ystart]=obj_beamv.createBeams(matrix)
            if(ystart>=675):
                break

    def createBeamss(self,matrix,xstart,ystart):
    
        while(True):
            obj_beams=BeamSla(xstart,ystart)
            [xstart,ystart]=obj_beams.createBeams(matrix)
            if(ystart>=675):
                break
    def createMagnet(self,matrix,xstart,ystart):

        obj_magnet=Magnet(xstart,ystart)
        obj_magnet.definemagnet()
        [self.__xmag,self.__ymag]=obj_magnet.createmagnet(matrix)

           
    def createSpeedBost(self,matrix,xstart,ystart):

        obj_speed=Speed(xstart,ystart)
        obj_speed.definespeed()
        obj_speed.createspeed(matrix)

