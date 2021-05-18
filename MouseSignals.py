import win32gui
import win32api
import win32con
# https://docs.microsoft.com/en-us/windows/win32/inputdev/mouse-input-notifications
import time

## finds the window handler for mr.mine's process
## if not found, returns -1

def getMrMineWindowHandler():
    hWndList = []
    win32gui.EnumWindows( getMrMineWindowEnumHandler, hWndList)

    if(not hWndList):
        print("ERROR - Mr.Mine window not found. Is the game running?")
        return -1
    else:
        return hWndList[0]

def getMrMineWindowEnumHandler(hWnd, list):

    if win32gui.GetWindowText(hWnd).find("Capacity:") != -1:
        list.append(hWnd)



# Simulates left click at position (x,y), in the window handled by hWnd
def leftClick(x, y, hWnd):

    lParam = win32api.MAKELONG(x, y)
    win32gui.SendMessage(hWnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
    win32gui.SendMessage(hWnd, win32con.WM_LBUTTONUP, None, lParam)

# Simulates right click at position (x,y), in the window handled by hWnd
def rightClick(x, y, hWnd):

    lParam = win32api.MAKELONG(x, y)
    win32gui.SendMessage(hWnd, win32con.WM_RBUTTONDOWN, win32con.MK_RBUTTON, lParam)
    win32gui.SendMessage(hWnd, win32con.WM_RBUTTONUP, None, lParam)

# Simulates key press, in the window handled by hWnd
# argument key should be a keycode, e.g VK_ESCAPE
# https://github.com/SublimeText/Pywin32/blob/master/lib/x32/win32/lib/win32con.py
def pressKey(key,hWnd):
    win32gui.SendMessage(hWnd,win32con.WM_KEYDOWN, key,0)
    win32gui.SendMessage(hWnd,win32con.WM_KEYUP, key,0)



handler = getMrMineWindowHandler()
print (handler)
x,y,w,h= win32gui.GetWindowRect(handler)
print(x,y,w,h)

SELLPOS = (int(0.225*w),int(0.5583*h))

leftClick(SELLPOS[0],SELLPOS[1],handler)
time.sleep(2)
pressKey(win32con.VK_ESCAPE,handler)


