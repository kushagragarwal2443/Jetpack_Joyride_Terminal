import os

class Board:

    def __init__(self,rows, columns):
        self.__rows=rows
        self.__columns=columns
        self.__matrix=[]
        self.__boardstring=""

    def getboardstring(self):
        return self.__boardstring
    def setboardstring(self,stringboard):
        self.__boardstring=stringboard

    def getBoarddim(self):
        return [self.__rows, self.__columns]
    def setBoarddim(self,rows,columns):
        self.__rows=rows
        self.__columns=columns

    def getMatrix(self):
        return self.__matrix
    def setMatrix(self,grid):
        self.__matrix=grid

    def createboard(self):
        
        for i in range(self.__rows):
            c=1
            temp=[]
            for j in range(self.__columns):
                temp.append(" ")
                c=c+1
                if(c==10):
                    c=1
            self.__matrix.append(temp)
        
    def printlines(self, leftmarg,rightmarg):
        boardstring=""
        for i in range(self.__rows):
            for j in range(leftmarg,rightmarg):
                boardstring=boardstring+self.__matrix[i][j]
                #print(self.__matrix[i][j], end="")
            #print()
            boardstring=boardstring+"\n"
    
        print(boardstring)


    def printboard(self, mandopos):

        if( mandopos>=0 and mandopos<=30):
            self.printlines(0,120)
        elif(mandopos>=self.__columns-120):
            self.printlines(self.__columns-120,self.__columns)
        else:
            self.printlines(mandopos-30, mandopos+90)



