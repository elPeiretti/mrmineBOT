from tkinter import *
from tkinter import ttk
import multiprocessing
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

bot_proc=0                    
PATH = os.path.dirname(os.path.realpath(__file__))   

def bot():
    

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

def setArmas():
    f=open(PATH+"/bin/opt.bin","r+")
    if(int(spin_armas.get())<10):
        f.write("0"+spin_armas.get())
    elif int(spin_armas.get())<13:
        f.write(spin_armas.get())
    
    f.close()

def boot():

    if(btn_inic['state'] == 'normal'):
        btn_inic.configure(bg="Gray73")
        btn_inic['state'] = 'disabled' 
        chk_chest['state'] = 'disabled'
        chk_pelea['state'] = 'disabled'
        chk_sellall['state'] = 'disabled'
        spin_armas['state'] = 'disabled'
        lbl_armas['state'] = 'disabled'
        setArmas()

        global bot_proc
        bot_proc=multiprocessing.Process(target=bot)
        bot_proc.daemon=True 
        bot_proc.start()

        btn_stop['state'] = 'normal'
        btn_stop.configure(bg="Red")
    
def pause():
    if(btn_stop['state'] == 'normal'):
        btn_stop.configure(bg="Gray73")
        btn_stop['state'] = 'disabled'

        global bot_proc
        bot_proc.terminate()
        bot_proc.join()

        btn_inic['state'] = 'normal'
        btn_inic.configure(bg="Green")
        btn_inic['state'] = 'normal' 
        chk_chest['state'] = 'normal'
        chk_pelea['state'] = 'normal'
        chk_sellall['state'] = 'normal'
        spin_armas['state'] = 'normal'
        lbl_armas['state'] = 'normal'

def setCofres():
    f=open(PATH+"/bin/opt.bin","r+")
    f.seek(3)
    if(chk_state_chest.get()):
        f.write("1")
    else:
        f.write("0")
    
    f.close()

def setPelea():
    f=open(PATH+"/bin/opt.bin","r+")
    f.seek(4)
    if(chk_state_pelea.get()):
        f.write("1")
    else:
        f.write("0")

    f.close()

def setVenta():
    
    f=open(PATH+"/bin/opt.bin","r+")
    f.seek(2)
    if(chk_state_sellall.get()):
        f.write("1")
    else:
        f.write("0")

    f.close()

def save():
    return



if __name__ == '__main__':

    f = open(PATH+"/bin/opt.bin","r+") #init opt.bin
    f.seek(2)
    f.write("000")
    f.close()

    window = Tk()
    window.geometry('100x130')
    window.title("Mr.Mine BOT")
    
    btn_inic = Button(window, text="Start",command=boot,bg="Green")
    btn_stop = Button(window, text="Stop",command=pause,bg="Gray")    

    btn_inic.grid(column=0, row=5)
    btn_stop['state']='disabled'
    btn_stop.grid(column=1, row=5)


    chk_state_sellall = IntVar()
    chk_state_chest = IntVar()
    chk_state_pelea = IntVar()
    chk_sellall = Checkbutton(window, text='Sell Everything',var=chk_state_sellall,onvalue=1, offvalue=0,command=setVenta)
    chk_chest = Checkbutton(window, text='Grab Chests',var=chk_state_chest,onvalue=1, offvalue=0,command=setCofres)
    chk_pelea = Checkbutton(window, text='Fight Monsters',var=chk_state_pelea,onvalue=1, offvalue=0,command=setPelea)

    chk_sellall.grid(columnspan=2, row=2)
    chk_chest.grid(columnspan=2, row=3)
    chk_pelea.grid(columnspan=2, row=4)


    lbl_armas = Label(window,text="Weapons:")
    lbl_armas.grid(column=0,row=1)

    spin_armas=Spinbox(window,from_=1,to=16,width=3)
    spin_armas.grid(column=1,row=1)

    window.mainloop()
