import os
import random
import time
from colorama import Fore, Back, init

class Mando:

    def __init__(self,xcod,ycod):
        self.__shape1 = [["|", Fore.YELLOW+'O'+ '\x1b[0m',"|"],[" ", Fore.RED+"\\"+'\x1b[0m', " "],[Fore.YELLOW+"^"+ '\x1b[0m', " ", Fore.YELLOW+"^"+ '\x1b[0m']]
        self.__shape2 = [[Back.YELLOW+Fore.WHITE+"|"+'\x1b[0m',Back.YELLOW+Fore.WHITE+ 'O'+'\x1b[0m',Back.YELLOW+Fore.WHITE+ "|"+'\x1b[0m'],[Back.YELLOW+Fore.WHITE+" "+'\x1b[0m', Back.YELLOW+Fore.WHITE+"\\"+'\x1b[0m',Back.YELLOW+Fore.WHITE+ "|"+'\x1b[0m'],[Back.YELLOW+Fore.WHITE+"^"+'\x1b[0m',Back.YELLOW+Fore.WHITE+ "^"+'\x1b[0m',Back.YELLOW+Fore.WHITE+ "|"+'\x1b[0m']]
        self.__shape3=[[" "," ",Back.RED+Fore.WHITE+"*"+'\x1b[0m'],[" ",Back.YELLOW+Fore.WHITE+"*"+'\x1b[0m'," "],[Back.YELLOW+Fore.WHITE+"*"+'\x1b[0m'," "," "]]
        self.__shape4=[[" ",Back.YELLOW+Fore.WHITE+"*"+'\x1b[0m'," "],[Back.YELLOW+Fore.WHITE+"*"+'\x1b[0m'," ",Back.RED+Fore.WHITE+"*"+'\x1b[0m'],[" "," "," "]]
        self.__shape5=[[Back.YELLOW+Fore.WHITE+"*"+'\x1b[0m'," "," "],[" ",Back.YELLOW+Fore.WHITE+"*"+'\x1b[0m'," "],[" "," ",Back.RED+Fore.WHITE+"*"+'\x1b[0m']]
        self.__shape6=[[" "," "," "],[Back.YELLOW+Fore.WHITE+"*"+'\x1b[0m'," ",Back.RED+Fore.WHITE+"*"+'\x1b[0m'],[" ",Back.YELLOW+Fore.WHITE+"*"+'\x1b[0m'," "]]
        self.__life=5
        self.__coin=0
        self.__x=xcod
        self.__y=ycod
        self.__speedboost=0
        self.__speedboostime=0
        self.__movingfast=0
        self.__shield=-1
        self.__mydrag=0
        self.__shieldtime=round(time.time())
        self.__gravmando=round(time.time())
    
    def getMyDrag(self):
        return self.__mydrag
    def setMyDrag(self,drag):
        self.__mydrag=drag
    
    
    def getMandolife(self):
        return self.__life
    def setMandolife(self,life):
        self.__life=life

    def getMandocoin(self):
        return self.__coin
    def setMandocoin(self,coin):
        self.__coin=coin
    
    def getMandocood(self):
        return [self.__x, self.__y]
    def setMandocood(self,x,y):
        self.__x=x
        self.__y=y

    def getspeedboost(self):
        return self.__speedboost
    def setspeedboost(self,speedboost):
        self.__speedboost=speedboost
    
    def getspeedboostime(self):
        return self.__speedboostime
    def setspeedboostime(self,speedboostime):
        self.__speedboostime=speedboostime

    def getshield(self):
        return self.__shield
    def setshield(self,shield):
        self.__shield=shield

    def getshieldtime(self):
        return self.__shieldtime
    def setshieldtime(self,shieldtime):
        self.__shieldtime=shieldtime

    def getmovingfast(self):
        return self.__movingfast
    def setmovingfast(self,value):
        self.__movingfast=value
    
    def printMando(self,matrix):

        self.checkcoins(matrix)
        if(self.__shield==0 or self.__shield ==-1 ):
            self.checkcol(matrix)

        if(self.__mydrag==1):
            
            if(self.__y%4 ==0):

                for i in range(self.__x -1, self.__x+2,1):
                    for j in range(self.__y-1, self.__y+2,1):
                        matrix[i][j]=self.__shape3[i-self.__x +1][j-self.__y+1]
            
            if(self.__y%4 ==1):

                for i in range(self.__x -1, self.__x+2,1):
                    for j in range(self.__y-1, self.__y+2,1):
                        matrix[i][j]=self.__shape4[i-self.__x +1][j-self.__y+1]

            if(self.__y%4 ==2):

                for i in range(self.__x -1, self.__x+2,1):
                    for j in range(self.__y-1, self.__y+2,1):
                        matrix[i][j]=self.__shape5[i-self.__x +1][j-self.__y+1]
            
            if(self.__y%4 ==3):

                for i in range(self.__x -1, self.__x+2,1):
                    for j in range(self.__y-1, self.__y+2,1):
                        matrix[i][j]=self.__shape6[i-self.__x +1][j-self.__y+1]




        elif(self.__shield==0 or self.__shield==-1):
            for i in range(self.__x -1, self.__x+2,1):
                for j in range(self.__y-1, self.__y+2,1):
                    matrix[i][j]=self.__shape1[i-self.__x +1][j-self.__y+1]
        elif(self.__shield ==1):
            for i in range(self.__x -1, self.__x+2,1):
                for j in range(self.__y-1, self.__y+2,1):
                    matrix[i][j]=self.__shape2[i-self.__x +1][j-self.__y+1]



    def deleteMando(self,matrix):
        for i in range(self.__x -1, self.__x+2,1):
            for j in range(self.__y-1, self.__y+2,1):
                matrix[i][j]=" "
    
    def checkcoins(self, matrix):
        x=self.__x
        y=self.__y
        if(matrix[x][y]==Fore.YELLOW +'$'+ '\x1b[0m'):
            self.__coin=self.__coin+1
        
        if(matrix[x][y+1]==Fore.YELLOW +'$'+ '\x1b[0m'):
            self.__coin=self.__coin+1
            
        if(matrix[x][y-1]==Fore.YELLOW +'$'+ '\x1b[0m'):
            self.__coin=self.__coin+1
        
        if(matrix[x-1][y-1]==Fore.YELLOW +'$'+ '\x1b[0m'):
            self.__coin=self.__coin+1
            
        if(matrix[x-1][y]==Fore.YELLOW +'$'+ '\x1b[0m'):
            self.__coin=self.__coin+1

        if(matrix[x-1][y+1]==Fore.YELLOW +'$'+ '\x1b[0m'):
            self.__coin=self.__coin+1   
            
        if(matrix[x+1][y+1]==Fore.YELLOW +'$'+ '\x1b[0m'):
            self.__coin=self.__coin+1
            
        if(matrix[x+1][y]==Fore.YELLOW +'$'+ '\x1b[0m'):
            self.__coin=self.__coin+1
        
        if(matrix[x+1][y-1]==Fore.YELLOW +'$'+ '\x1b[0m'):
            self.__coin=self.__coin+1

        
        #for fast moving mando
        

    def activategravity(self):
        currtime=round(time.time())
        if(currtime-self.__gravmando<=0.4):
            self.__x=self.__x + 1
        elif(currtime - self.__gravmando <=0.8):
            self.__x = self.__x +2
        else:
            self.__x = self.__x + 3

        if(self.__x >=26):
            self.__x=26

    def deactivategravity(self,time):
        self.__gravmando=time


    def checkcol(self, matrix):
        x=self.__x
        y=self.__y
        if(self.__mydrag==1):

            if(matrix[x][y]==Back.CYAN + Fore.CYAN+'*'+'\x1b[0m' or matrix[x][y]==Back.RED + Fore.WHITE+'*'+'\x1b[0m'):
                self.__mydrag=-1

            if(matrix[x][y+1]==Back.CYAN + Fore.CYAN+'*'+'\x1b[0m' or matrix[x][y+1]==Back.RED + Fore.WHITE+'*'+'\x1b[0m'):
                self.__mydrag=-1
            
            if(matrix[x][y-1]==Back.CYAN + Fore.CYAN+'*'+'\x1b[0m' or matrix[x][y-1]==Back.RED + Fore.WHITE+'*'+'\x1b[0m'):
                self.__mydrag=-1

            if(matrix[x+1][y]==Back.CYAN + Fore.CYAN+'*'+'\x1b[0m' or matrix[x+1][y]==Back.RED + Fore.WHITE+'*'+'\x1b[0m'):
                self.__mydrag=-1

            if(matrix[x+1][y+1]==Back.CYAN + Fore.CYAN+'*'+'\x1b[0m' or matrix[x+1][y+1]==Back.RED + Fore.WHITE+'*'+'\x1b[0m'):
                self.__mydrag=-1
            
            if(matrix[x+1][y-1]==Back.CYAN + Fore.CYAN+'*'+'\x1b[0m' or matrix[x+1][y-1]==Back.RED + Fore.WHITE+'*'+'\x1b[0m'):
                self.__mydrag=-1

            if(matrix[x-1][y]==Back.CYAN + Fore.CYAN+'*'+'\x1b[0m' or matrix[x-1][y]==Back.RED + Fore.WHITE+'*'+'\x1b[0m'):
                self.__mydrag=-1

            if(matrix[x-1][y+1]==Back.CYAN + Fore.CYAN+'*'+'\x1b[0m' or matrix[x-1][y+1]==Back.RED + Fore.WHITE+'*'+'\x1b[0m'):
                self.__mydrag=-1
            
            if(matrix[x-1][y-1]==Back.CYAN + Fore.CYAN+'*'+'\x1b[0m' or matrix[x-1][y-1]==Back.RED + Fore.WHITE+'*'+'\x1b[0m'):
                self.__mydrag=-1

                
        else:

            if(matrix[x][y]==Back.CYAN + Fore.CYAN+'*'+'\x1b[0m' or matrix[x][y]==Back.RED + Fore.WHITE+'*'+'\x1b[0m'):
                self.__life=self.__life-1

            if(matrix[x][y+1]==Back.CYAN + Fore.CYAN+'*'+'\x1b[0m' or matrix[x][y+1]==Back.RED + Fore.WHITE+'*'+'\x1b[0m'):
                self.__life=self.__life-1
            
            if(matrix[x][y-1]==Back.CYAN + Fore.CYAN+'*'+'\x1b[0m' or matrix[x][y-1]==Back.RED + Fore.WHITE+'*'+'\x1b[0m'):
                self.__life=self.__life-1

            if(matrix[x+1][y]==Back.CYAN + Fore.CYAN+'*'+'\x1b[0m' or matrix[x+1][y]==Back.RED + Fore.WHITE+'*'+'\x1b[0m'):
                self.__life=self.__life-1

            if(matrix[x+1][y+1]==Back.CYAN + Fore.CYAN+'*'+'\x1b[0m' or matrix[x+1][y+1]==Back.RED + Fore.WHITE+'*'+'\x1b[0m'):
                self.__life=self.__life-1
            
            if(matrix[x+1][y-1]==Back.CYAN + Fore.CYAN+'*'+'\x1b[0m' or matrix[x+1][y-1]==Back.RED + Fore.WHITE+'*'+'\x1b[0m'):
                self.__life=self.__life-1

            if(matrix[x-1][y]==Back.CYAN + Fore.CYAN+'*'+'\x1b[0m' or matrix[x-1][y]==Back.RED + Fore.WHITE+'*'+'\x1b[0m'):
                self.__life=self.__life-1

            if(matrix[x-1][y+1]==Back.CYAN + Fore.CYAN+'*'+'\x1b[0m' or matrix[x-1][y+1]==Back.RED + Fore.WHITE+'*'+'\x1b[0m'):
                self.__life=self.__life-1
            
            if(matrix[x-1][y-1]==Back.CYAN + Fore.CYAN+'*'+'\x1b[0m' or matrix[x-1][y-1]==Back.RED + Fore.WHITE+'*'+'\x1b[0m'):
                self.__life=self.__life-1

        
    def checkballcol(self,balls):
        x=self.__x
        y=self.__y

        for i in range(100):
            if(balls[i]["enable"]==1):

                if((y+1==balls[i]['y'] and x==balls[i]['x']) or (y==balls[i]['y'] and x==balls[i]['x'])):
                    self.__life=self.__life-1
                    balls[i]["enable"]=0
                if((y+1==balls[i]['y'] and x+1==balls[i]['x']) or (y==balls[i]['y'] and x+1==balls[i]['x'])):
                    self.__life=self.__life-1
                    balls[i]["enable"]=0
                if((y+1==balls[i]['y'] and x-1==balls[i]['x']) or (y==balls[i]['y'] and x-1==balls[i]['x'])):
                    self.__life=self.__life-1
                    balls[i]["enable"]=0
                if((y-1==balls[i]['y'] and x+1==balls[i]['x']) or (y==balls[i]['y'] and x+1==balls[i]['x'])):
                    self.__life=self.__life-1
                    balls[i]["enable"]=0
                if((y-1==balls[i]['y'] and x-1==balls[i]['x']) or (y==balls[i]['y'] and x-1==balls[i]['x'])):
                    self.__life=self.__life-1
                    balls[i]["enable"]=0
                

        return balls



   



 