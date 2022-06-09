from pynput.keyboard import Key
from pynput.mouse import Button
from pynput.mouse import Controller as mouseController
from pynput.keyboard import Controller as keyboardController
import time

keyboard = keyboardController()
mouse = mouseController()

def web(link):
    mouse.position = (10,1500)
    mouse.click(Button.left)
    time.sleep(1)
    keyboard.type("Google Chrome")
    time.sleep(1)
    keyboard.press(Key.enter)
    time.sleep(2)
    keyboard.type(link)
    time.sleep(1)
    keyboard.press(Key.enter)

def autoclicker(click_szam, click_közti_ido):
    time.sleep(3)
    for _ in range(click_szam):
        mouse.click(Button.left)
        time.sleep(click_közti_ido)

#web("https://www.youtube.com/watch?v=dQw4w9WgXcQ") #rickroll

def autoclicker_web():
    web("https://cpstest.org")
    mouse.position = (1000,800)
    autoclicker(100, 0.02)

autoclicker_web()