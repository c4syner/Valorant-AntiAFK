import pynput
from pynput.mouse import Button
from pynput import mouse
import random
import time

mouseActive = pynput.mouse.Controller()

coord = (0,0)

def on_move(x, y):
    global coord
    coord = x,y

def on_click(x, y, button, pressed):
    pass

def on_scroll(x, y, dx, dy):
    pass
listener = mouse.Listener(
    on_move=on_move,
    on_click=on_click,
    on_scroll=on_scroll)
listener.start()
def stayAlive():
    mouseActive.press(Button.left)
    mouseActive.release(Button.left)

while(True):
    thisCoord = coord
    time.sleep(10)
    if(thisCoord == coord):
        print("AFK Detected...")
        stayAlive()
    else:
        print("User AK")