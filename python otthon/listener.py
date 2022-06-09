from pynput.mouse import Listener
import logging

logging.basicConfig(filename="mouse_log.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")

def on_move(x,y):
    logging.info(f"Mouse moved to ({x}, {y})")

def on_click(x, y, button, pressed):
    logging.info(f"Mouse click az ({x}, {y} with {button})")

def on_scroll(x, y, dx, dy):
    logging.info(f"Mouse scrolled at ({x}, {y}, {dx}, {dy})")

with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()