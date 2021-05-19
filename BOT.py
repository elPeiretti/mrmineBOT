import pyautogui
from python_imagesearch.imagesearch import imagesearch
from python_imagesearch.imagesearch import imagesearcharea
import PIL.ImageGrab
from PIL import ImageChops
from PIL import Image
import pyscreenshot as ImageGrab
import cv2
import time
import os

PATH = os.path.dirname(os.path.realpath(__file__))  

def process():
    
    f = open(PATH+"/bin/opt.bin","r")
    ARMAS=int(f.readline(2))
    SELLALL = int(f.readline(1))
    COFRES = int(f.readline(1))
    FIGHT= int(f.readline(1))
    f.close()

    pyautogui.PAUSE=0.01

    def estaAlfinal():
        #global PATH
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
            pyautogui.PAUSE=0.1
            pyautogui.moveTo(posx+10, posy+10)
            pyautogui.click()
            pyautogui.moveTo(960, 540)
            pyautogui.click()
            pyautogui.click()
            pyautogui.PAUSE=0.01
            return True
        else:
            return False

    def estaLleno():
        pos = imagesearch(PATH+'/bin/pics/lleno.png')
        pos2 = imagesearch(PATH+'/bin/pics/lleno2.png')
        if pos[0] != -1 or pos2[0]!=-1:
            return True
        else:
            return False


    def venderTodo():
        if (estaLleno()):
            pix=0
            pyautogui.click(446, 624)
            time.sleep(1)
            for x in range (1,13):
                pyautogui.click(627, 309+pix)
                pix+=34
            pyautogui.click(1407, 282)

    def venderTodo2():
        time.sleep(0.1)
        pyautogui.moveTo(446, 624)
        pyautogui.click()
        time.sleep(0.3)
        pyautogui.moveTo(627,750)
        pyautogui.click()  
        pyautogui.moveTo(1407, 282)
        pyautogui.click()

    def tocarWachines():
        y=0
        for i in range(0,5):
            x=0
            for j in range(0,10):
                pyautogui.click(187+x,250+y)
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
                    pyautogui.click(x,y)
                    y+=47
                x+=202



    time.sleep(1)

    while True:
        
        layer=0
        pyautogui.moveTo(134, 209)
        pyautogui.click()
        if(SELLALL):
            venderTodo2()
        
        while not (estaAlfinal()): #mientras no este en el final, busco wachines
        
            while COFRES and hayCofre():
                pass #hayCofre picks up the chest

            if FIGHT and layer>304:
                pyautogui.PAUSE=0.005
                tocarWachines()
                pyautogui.PAUSE=0.01
                pelear()
                

            pyautogui.press('down',4)#bajar
            layer+=4
