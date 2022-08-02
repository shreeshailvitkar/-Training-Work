import time
import os
import webbrowser
import pyautogui as pg
from pynput.keyboard import Key, Controller as K
from pynput.mouse import Button, Controller as M
'''
os.startfile("notepad.exe")
M().position = (900,400)
M().click(Button.left, 1)
#time.sleep(3)
for i in range(30):
    K().type('Hello world!')
    time.sleep(60)
'''
pg.write('shree')