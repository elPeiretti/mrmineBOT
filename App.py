from tkinter import *
from tkinter import ttk
import multiprocessing
import bot

bot_proc=0
PATH = bot.PATH               

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
        bot_proc=multiprocessing.Process(target=bot.process)
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
