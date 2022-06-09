import time
from pynput.keyboard import Controller, Key

kb = Controller()

def spam(x):
        for _ in range(x):
            time.sleep(3)
            kb.type('You should call me "senpaii", ')
            kb.type('Play it like a hentai')
            kb.press(Key.enter)
            time.sleep(0.2)

spam(10)