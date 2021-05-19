from python_imagesearch.imagesearch import imagesearch
from python_imagesearch.imagesearch import imagesearcharea
import PIL.ImageGrab
from PIL import ImageChops
from PIL import Image
import pyscreenshot as ImageGrab
import cv2
import time
import os

from win32con import VK_DOWN
import InputEmulation

PATH = os.path.dirname(os.path.realpath(__file__))  
hWnd = InputEmulation.getWindowHandlersContaining("Capacity:")

def process():

    global hWnd

    if not hWnd:
        print("ERROR - MR MINE WINDOW NOT FOUND. IS THE GAME RUNNING?")
        return
    else:
        hWnd = hWnd[0]

    f = open(PATH+"/bin/opt.bin","r")
    ARMAS=int(f.readline(2))
    SELLALL = int(f.readline(1))
    COFRES = int(f.readline(1))
    FIGHT= int(f.readline(1))
    f.close()


    def estaAlfinal():
        pos = imagesearch(PATH+'/bin/pics/standar2.png',0.97) 
        if pos[0] != -1:
            return True
        else:
            return False

    def hayCofre(): 
        pos = imagesearch(PATH+'/bin/pics/cofre.png') 
        if pos[0] != -1:
            posx=pos[0]
            posy=pos[1]
            InputEmulation.moveCursor(posx+10, posy+10,hWnd)
            InputEmulation.leftClick(posx+10, posy+10,hWnd)
            InputEmulation.moveCursor(920, 610,hWnd)
            InputEmulation.leftClick(920, 610,hWnd)
            InputEmulation.leftClick(920, 610,hWnd)
            return True
        else:
            return False


    def venderTodo():
        
        pix=0
        InputEmulation.moveCursor(446, 624,hWnd)
        InputEmulation.leftClick(446, 624,hWnd)

        for x in range (1,13):
            InputEmulation.moveCursor(627, 309+pix,hWnd)
            InputEmulation.leftClick(627, 309+pix,hWnd)
            pix+=34
        InputEmulation.moveCursor(1407, 264, hWnd)
        InputEmulation.leftClick(1407, 264, hWnd)

    
    def tocarWachines():
        y=0
        for i in range(0,5):
            x=0
            for j in range(0,10):
                InputEmulation.moveCursor(187+x,250+y,hWnd)
                InputEmulation.leftClick(187+x,250+y,hWnd)
                x+=138
            y+=177

    def hayPelea():
        
        pos = imagesearch(PATH+'/bin/pics/fist.png') 
        if pos[0] != -1:
            return True
        else:
            return False

    def pelear():
        cant=int(ARMAS/4)
        if(ARMAS%4!=0):
            cant+=1
        
        while hayPelea():
            x=535
            for j in range(0,cant):
                y=653
                for i in range(0,4):
                    InputEmulation.moveCursor(x,y,hWnd)
                    InputEmulation.leftClick(x,y,hWnd)
                    y+=47
                x+=202


    while True:
        layer=0
        
        InputEmulation.moveCursor(109,200,hWnd)
        InputEmulation.leftClick(109,200,hWnd)

        if(SELLALL):
            venderTodo()
        
        while not (estaAlfinal()): #mientras no este en el final, busco wachines
        
            while COFRES and hayCofre():
                pass #hayCofre picks up the chest

            if FIGHT and layer>304:
                tocarWachines()
                pelear()
                
            for x in range (0,4):
                InputEmulation.pressKey(VK_DOWN,hWnd) #bajar
            layer+=4
