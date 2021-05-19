import win32gui
import win32api
import win32con
# https://docs.microsoft.com/en-us/windows/win32/inputdev/mouse-input-notifications
import time

## finds the window handler for mr.mine's process
## if not found, returns -1


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

# returns the window's handler named WindowName
# returns 0 if not found

def getWindowHandlerByName(WindowName):
    return win32gui.FindWindow(None,WindowName)


# returns a list of all the windows handlers that contains WindowName in their names
# WindowName argument is a String type

def getWindowHandlersContaining(WindowName):
    
    hWndList = []

    win32gui.EnumWindows( lambda hWnd,list:  list.append(hWnd), hWndList)

    return list(filter(lambda h: win32gui.GetWindowText(h).find(WindowName)!=-1, hWndList))


hWnd = getWindowHandlersContaining("Capacity:")
handler = hWnd[0]
print (handler)
x,y,w,h= win32gui.GetWindowRect(handler)
print(x,y,w,h)

#SELLPOS = (int(0.225*w),int(0.5583*h))

#leftClick(SELLPOS[0],SELLPOS[1],handler)
#time.sleep(2)
#pressKey(win32con.VK_ESCAPE,handler)

