import os
from colorama import Fore, Back, init
import signal
import time



from getch import _getChUnix as getChar
from coins import Coins
from board import Board
from scenery import Scenery
from mando import Mando
from alarmexception import AlarmException
from dragon import Dragon
from bullets import Bullets
from dragonball import Dragonball

obj_board= Board(30,800)
obj_board.createboard()
matrix=obj_board.getMatrix()



obj_scenery = Scenery()
obj_scenery.createGround(matrix)
obj_scenery.createSky(matrix)
obj_scenery.createClouds(matrix,4,25)
obj_scenery.createCoins(matrix,15,45)
obj_scenery.createBeamsh(matrix,15,25)
obj_scenery.createBeamsv(matrix,10,45)
obj_scenery.createBeamss(matrix,10,65)
obj_scenery.createMagnet(matrix,7,205)
obj_scenery.createSpeedBost(matrix,14,300)

obj_dragon=Dragon(5,754)
obj_dragon.createDragon()

obj_bullet=Bullets()

obj_board.setMatrix(matrix)


obj_mando = Mando(26,1)
#obj_mando.starting_position(obj_board.matrix)

obj_dragonball=Dragonball()



os.system('clear')
print("\n\n\n\n")
with open("./background/welx.txt") as welcometext:
    for line in welcometext:
        print("\t\t"+Fore.YELLOW+line.strip("\n")+'\x1b[0m')

time.sleep(4)

os.system('clear')

def checkbullball():
    bullets=obj_bullet.getbullet()
    balls=obj_dragonball.getball()
    for i in range(100):
        for j in range(100):
            

            if(bullets[i]["enable"]==1 and bullets[i]["x"]==balls[j]["x"] and bullets[i]["y"]==balls[j]["y"] and balls[j]["enable"]==1):
                bullets[i]["enable"]=0
                balls[j]["enable"]=0
            elif(bullets[i]["enable"]==1 and bullets[i]["x"]==balls[j]["x"] and (bullets[i]["y"]+1)==balls[j]["y"] and balls[j]["enable"]==1):
                bullets[i]["enable"]=0
                balls[j]["enable"]=0
            elif(bullets[i]["enable"]==1 and bullets[i]["x"]==balls[j]["x"] and (bullets[i]["y"]+2)==balls[j]["y"] and balls[j]["enable"]==1):
                bullets[i]["enable"]=0
                balls[j]["enable"]=0
            elif(bullets[i]["enable"]==1 and bullets[i]["x"]==balls[j]["x"] and (bullets[i]["y"]+3)==balls[j]["y"] and balls[j]["enable"]==1):
                bullets[i]["enable"]=0
                balls[j]["enable"]=0
    obj_bullet.setbullet(bullets)
    obj_dragonball.setball(balls)

def printdonotcross():

    matrix=obj_board.getMatrix()

    matrix[4][750]='D'    
    matrix[5][750]='O'    
    matrix[6][750]=' '    
    matrix[7][750]='N'    
    matrix[8][750]='O'    
    matrix[9][750]='T'    
    matrix[10][750]=' '    
    matrix[11][750]='C'    
    matrix[12][750]='R'    
    matrix[13][750]='O' 
    matrix[14][750]='S'    
    matrix[15][750]='S'    
    matrix[16][750]=' '    
    matrix[17][750]='T'    
    matrix[18][750]='H'       
    matrix[19][750]='I' 
    matrix[20][750]='S'    
    matrix[21][750]=' '    
    matrix[22][750]='L'  
    matrix[23][750]='I'    
    matrix[24][750]='N'    
    matrix[25][750]='E'     

    obj_board.setMatrix(matrix)    

def speedbooster():
    [x,y]=obj_mando.getMandocood()
    speedboost=obj_mando.getspeedboost()
    speedbooster=obj_mando.getspeedboostime()

    if(matrix[x][y]==Back.MAGENTA + Fore.MAGENTA+'@'+ '\x1b[0m'):
        speedboost=1
        speedbooster=round(time.time())

    if(matrix[x][y+1]==Back.MAGENTA + Fore.MAGENTA+'@'+ '\x1b[0m'):
        speedboost=1
        speedbooster=round(time.time())
    
    if(matrix[x][y-1]==Back.MAGENTA + Fore.MAGENTA+'@'+ '\x1b[0m'):
        speedboost=1
        speedbooster=round(time.time())

    if(matrix[x+1][y]==Back.MAGENTA + Fore.MAGENTA+'@'+ '\x1b[0m'):
        speedboost=1
        speedbooster=round(time.time())

    if(matrix[x+1][y+1]==Back.MAGENTA + Fore.MAGENTA+'@'+ '\x1b[0m'):
        speedboost=1
        speedbooster=round(time.time())
    
    if(matrix[x+1][y-1]==Back.MAGENTA + Fore.MAGENTA+'@'+ '\x1b[0m'):
        speedboost=1
        speedbooster=round(time.time())

    if(matrix[x-1][y]==Back.MAGENTA + Fore.MAGENTA+'@'+ '\x1b[0m'):
        speedboost=1
        speedbooster=round(time.time())

    if(matrix[x-1][y+1]==Back.MAGENTA + Fore.MAGENTA+'@'+ '\x1b[0m'):
        speedboost=1
        speedbooster=round(time.time())
    
    if(matrix[x-1][y-1]==Back.MAGENTA + Fore.MAGENTA+'@'+ '\x1b[0m'):
        speedboost=1
        speedbooster=round(time.time())

    obj_mando.setspeedboost(speedboost)
    obj_mando.setspeedboostime(speedbooster)



def shield():
    shield=obj_mando.getshield()
    shieldtime=obj_mando.getshieldtime()

    if(shield==0):
        if(round(time.time())- shieldtime >=70):
            shield=1
            shieldtime=round(time.time())
    
    if(shield==-1):
        shield=1
        shieldtime=round(time.time())
    

    obj_mando.setshield(shield)
    obj_mando.setshieldtime(shieldtime)




def magnetism():
    
    #change coordinates of magnet form topleftmost to central coordinates to facilitate calculations
    [xmag,ymag]=obj_scenery.getMagCood()
    
    #force is in the direction of the vector from the magnet to the central coordinates of the mando
    [x,y]=obj_mando.getMandocood()

    diffy=ymag-y
    diffx=xmag-x
    val=0

    if(diffy<30 and diffy>-15  and abs(diffx)<30):

        obj_mando.deactivategravity(round(time.time()))

        if(diffy!=0):
            ratios=abs(diffx/diffy)

            if(ratios <0.5):
                #diffy>>diffx so we need not reduce direction in the x frame right now
                #ymag >y, i.e the magnet is towards the right of the mando
                if(diffy >=0):
                    y=y+3
                    val=0
               
            
            elif(ratios>2 ):
                #diffx >> diffy, so only change direction in the x frame
                if( diffx >0):
                    #xmag >x, i.e the magnet is below the mando
                    x=x+0
                    val=0
                else:
                    x=x-3
                    val=0
            
            else:
                #the difference in both is comparable hence both the frames should be affected
                if(diffy >0):
                    y=y+3
                    val=0
                if(diffx>0):
                    x=x+0
                    val=0
                else:
                    x=x-3
                    val=0

            if(diffy<0):
                y=y-1
                val=1

    obj_mando.setMandocood(x,y)

    return val
            







def movemando(char):
    [x,y]=obj_mando.getMandocood()
    
    if(char=='w'):
        x=x-4
        if(x<=2):
            x=2
    
    if(char=='a'):
       y=y-4
       if(y<=1):
           y=1
    
    if(char=='s'):
        x=x+3
        if(x>26):
            x=26
    
    if(char =='d'):
        y=y+2
        obj_mando.setmovingfast(1)
        if(y>=798):
            y=798

    obj_mando.setMandocood(x,y)


def take_input():

    def alarmhandler(signum, frame):
        raise AlarmException

    def user_input(timeout=0.05):
        signal.signal(signal.SIGALRM, alarmhandler)
        signal.setitimer(signal.ITIMER_REAL, timeout)

        try:
            text = getChar()()
            signal.alarm(0)
            return text
        except AlarmException:
            pass
        signal.signal(signal.SIGALRM, signal.SIG_IGN)
        return ''
    return user_input()


start_time=time.time()


bulletcount=0

dragonballcount=0
timeballcount=0

stringis=""

while(True):

    #print('\033[0;0H')
    os.system('clear')
    stringis=""
    timerem = 150 - (round(time.time()) - round(start_time))
    stringis=stringis + "TIME REMAINING:"+ str(timerem) +'          '
    stringis=stringis + "LIVES:"+ str(obj_mando.getMandolife())+'           '
    stringis=stringis + "COINS:"+ str(obj_mando.getMandocoin()+ obj_bullet.getdragonscore())+'          '
    stringis=stringis +"BULLETS:"+str(100-bulletcount)+'        '
    stringis=stringis +"DRAGON LIVES:"+str(obj_bullet.getdragonlife())+"\n"
    

    stringis=stringis + "SPEEDBOSTER MODE:"+str(obj_mando.getspeedboost())+'        ' 
    #print("SPEEDBOSTER MODE:",obj_mando.getspeedboost(), end='\t  ' )

    if(obj_mando.getspeedboost()==1 and (round(time.time())-obj_mando.getspeedboostime())>10):
        obj_mando.setspeedboost(0) 
    if(obj_mando.getspeedboost() ==1):
        stringis=stringis + "SPEEDBOOST TIME REM:"+str(10-(round(time.time())- obj_mando.getspeedboostime()))+'        ' 
        #print("SPEEDBOOST TIME REM:", (10-(round(time.time())- obj_mando.getspeedboostime())), end="\t  ")
    
    
    
    if(obj_mando.getshield()==-1):
        stringis=stringis+"SHIELD MODE: 0" + '        ' 
        stringis=stringis+"SHIELD AVAILABLE" + '        '
        #print("SHIELD MODE:","0", end='\t  ' )
        #print("SHIELD AVAILABLE", end="\t  ")
    else:
        stringis=stringis + "SHIELD MODE:"+str(obj_mando.getshield())+'        ' 
        #print("SHIELD MODE:",obj_mando.getshield(), end='\t  ' )

    if(obj_mando.getshield()==1 and (round(time.time())-obj_mando.getshieldtime())>10):
        obj_mando.setshield(0) 
    if(obj_mando.getshield() ==1):
        stringis=stringis + "SHIELD TIME REM:"+str(10-(round(time.time())- obj_mando.getshieldtime()))+'        ' 
        #print("SHIELD TIME REM:", (10-(round(time.time())- obj_mando.getshieldtime())), end="\t  ")
        
    if(obj_mando.getshield() ==0):
        shieldtimerem=70-(round(time.time())- obj_mando.getshieldtime())
        if(shieldtimerem<0):
            shieldtimerem=0
        stringis=stringis + "NEXT SHIELD AVAILABLE IN:"+str(shieldtimerem)+'        ' 
        #print("NEXT SHIELD AVAILABLE IN:", shieldtimerem, end="\t  " )

    stringis=stringis
    #print()
    matrix=obj_board.getMatrix()

    speedbooster()
    val=magnetism()
    [x,y]=obj_mando.getMandocood()

    
    obj_mando.printMando(matrix)
    obj_mando.setmovingfast(0)
    
    obj_dragon.printDragon(matrix)
    obj_board.setMatrix(matrix)


   
    checkbullball()
    if(obj_mando.getshield()!=1):
        ball=obj_mando.checkballcol(obj_dragonball.getball())
        obj_dragonball.setball(ball)
    
    obj_bullet.timeincreased()
    obj_dragonball.timeincreased()
    matrix=obj_bullet.checkbullcoll(obj_board.getMatrix())
    obj_board.setMatrix(matrix)
    obj_bullet.expirebullet()

    printdonotcross()
    [x,y]=obj_mando.getMandocood()
    if(y>=750):
        life=obj_mando.getMandolife()
        obj_mando.setMandolife(life-1)

    
    matrix=obj_bullet.addbullettoboard(obj_board.getMatrix())
    obj_dragonball.addballtoboard(matrix)
    obj_board.setMatrix(matrix)
    
    print(stringis)
    obj_board.printboard(y)
    

    time.sleep(0.15)
    
   
    matrix=obj_board.getMatrix()
    obj_mando.deleteMando(matrix)
    obj_dragonball.removeballfromboard(matrix)
    obj_bullet.removebulletfromboard(matrix)
    obj_dragon.delDragon(matrix)
    obj_board.setMatrix(matrix)
    
    speedboost=obj_mando.getspeedboost()
    speedboostime=obj_mando.getspeedboostime()
    [x,y]=obj_mando.getMandocood()
    obj_mando.setMandocood(x,y+1)
    
    [x,y]=obj_mando.getMandocood()
    if(y>692 or val==1):
        obj_mando.setMandocood(x,y-1)
    if(val==1 and char=='d'):
        obj_mando.setMandocood(x,y+1)
    if(speedboost==1 and (round(time.time())- speedboostime)<=10 ):
        [x,y]=obj_mando.getMandocood()
        obj_mando.setMandocood(x,y+2)

    [x,y]=obj_mando.getMandocood()
    if ( x>= 26):
        obj_mando.setMandocood(26,y)
    
    
    [rows,columns]=obj_board.getBoarddim()
    matrix=obj_board.getMatrix()
    if(y>=columns or timerem==0):
        break
    
   
    char = take_input()

    movemando(char)
    obj_dragon.Dragmove(x)


    [dragonx,dragony]=obj_dragon.getDragcood()

    if(y>=680):
        if(timeballcount%20==0):
            obj_dragonball.firebullets(dragonballcount,dragonx,dragony-22)
            obj_dragonball.firebullets(dragonballcount+1,dragonx-6,dragony-14)
            obj_dragonball.firebullets(dragonballcount+2,dragonx+6,dragony-14)
            dragonballcount=dragonballcount+3

        timeballcount+=1



    [x,y]=obj_mando.getMandocood()
    if(char =='m' and bulletcount<=99):
        obj_bullet.firebullets(bulletcount,x,y+2)
        bulletcount=bulletcount+1
    
    if(char =='w' or char=='s'):
        obj_mando.deactivategravity(round(time.time()))
    obj_mando.activategravity()

    if(char==' '):
        shield()

    if(char=='f' and obj_mando.getMyDrag()==0 and y<=680):
        obj_mando.setMyDrag(1)

    if(char=='q'):
        os.system('clear')
        print("\n\n\n\n")
        with open("./background/quit.txt") as welcometext:
            for line in welcometext:
                print("\t\t\t\t"+Fore.RED+line.strip("\n")+'\x1b[0m')
        print("\n\n")        
        print("\t\t\t\t\t\t\tFinal Score:", obj_mando.getMandocoin() + obj_bullet.getdragonscore(),  "\n\n\n\n\n\n")
        break

    life=obj_mando.getMandolife()
    if(life<=0 or timerem<=1):
        os.system('clear')
        print("\n\n\n\n")
        with open("./background/lost.txt") as welcometext:
            for line in welcometext:
                print("\t\t\t\t"+Fore.RED+line.strip("\n")+'\x1b[0m')
        print("\n\n")        
        print("\t\t\t\t\t\t\tFinal Score:", obj_mando.getMandocoin() + obj_bullet.getdragonscore(),  "\n\n\n\n\n\n")
        break

    if(obj_bullet.getdragonlife()<=0):
        os.system('clear')
        print("\n\n\n\n")
        with open("./background/won.txt") as welcometext:
            for line in welcometext:
                print("\t\t\t\t"+Fore.GREEN+line.strip("\n")+'\x1b[0m')
        print("\n\n")        
        print("\t\t\t\t\t\t\tFinal Score:", obj_mando.getMandocoin() + obj_bullet.getdragonscore(),  "\n\n\n\n\n\n")
        break
    

    

    

    



    