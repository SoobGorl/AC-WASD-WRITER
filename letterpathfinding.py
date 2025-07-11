import time
import pyautogui
from letters import *
key_delay = 0.5
# time between stick presses
letter_delay = 0.5
# time between letters

def up():
    time.sleep(key_delay)
    pyautogui.press("w")
    print("W PRESS (1 / UP)")
def left():
    time.sleep(key_delay)
    pyautogui.press("a")
    print("A PRESS (3 / LEFT)")
def down():
    time.sleep(key_delay)
    pyautogui.press("s")
    print("S PRESS (2 / DOWN)")
def right():
    time.sleep(key_delay)
    pyautogui.press("d")
    print("D PRESS (4 / RIGHT)")
def select():
    time.sleep(key_delay)
    pyautogui.press("e")
    print("SELECTING " + letter_changer[0] + " (A PRESS)")
    time.sleep(letter_delay)

# STUPID AND LOOPS!!!!!!!!! THESE ALL DO THE SAME THING!!! BUT I DON'T KNOW HOW TO MAKE letter_trans_# and path_# MALUABLE!!!!!!

def letter_trans_a():
    for lister_func in path_a:
        if lister_func == 1:
            up()
        elif lister_func == 2:
            down()
        elif lister_func == 3:
            left()
        elif lister_func == 4:
            right()
def letter_trans_b():
    for lister_func in path_b:
        if lister_func == 1:
            up()
        elif lister_func == 2:
            down()
        elif lister_func == 3:
            left()
        elif lister_func == 4:
            right()
def letter_trans_c():
    for lister_func in path_c:
        if lister_func == 1:
            up()
        elif lister_func == 2:
            down()
        elif lister_func == 3:
            left()
        elif lister_func == 4:
            right()
def rank_reset():
    [x - 1 for x in path_c]
    print("! RESET !")
    for lister_func in path_c:
        if lister_func == 1:
            up()
        elif lister_func == 2:
            down()
        elif lister_func == 3:
            left()
        elif lister_func == 4:
            right()
    print("! RESET FINISHED !")
letter_changer = ["NULL"]
def new_letter_printer():
    print("TARGETING " + letter_changer[0])
