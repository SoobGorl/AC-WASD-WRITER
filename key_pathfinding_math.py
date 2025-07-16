import time
import pydirectinput
from key_paths import *

debug = False

key_delay = 0
# time between stick presses
letter_delay = 0
# time between letters

def caps_toggle(): # toggles caps (not on or off, just an input)
    pydirectinput.press("g")
    print("!!! TOGGLING CAPS !!!")

# WASD DIRECTIONS
def up():
    time.sleep(key_delay)
    print("W PRESS (1 / UP)")
    pydirectinput.press("w")
def left():
    time.sleep(key_delay)
    print("A PRESS (3 / LEFT)")
    pydirectinput.press("a")
def down():
    time.sleep(key_delay)
    print("S PRESS (2 / DOWN)")
    pydirectinput.press("s")
def right():
    time.sleep(key_delay)
    print("D PRESS (4 / RIGHT)")
    pydirectinput.press("d")
def select():
    time.sleep(key_delay)
    letter_changer[0] = "E"
    print("SELECTING " + letter_changer[0] + " (A PRESS)")
    pydirectinput.press("e")
    time.sleep(letter_delay)

letter_changer = ["NULL"]

def new_letter_printer():
    print("TARGETING " + letter_changer[0])

def letter_trans(letters_call):
    for lister_func in letters_call:
        if lister_func == 1:
            up()
        elif lister_func == 2:
            down()
        elif lister_func == 3:
            left()
        elif lister_func == 4:
            right()

def rank_reset(letters_call):
    print("! RESET !")
    rank_reverser = list(map(lambda x: x - 1, letters_call))
    rank_reverser.reverse()
    for lister_func in rank_reverser:
        if lister_func == 1:
            up()
        elif lister_func == 2:
            down()
        elif lister_func == 3:
            left()
        elif lister_func == 4:
            right()
        else:
            print("????? INVALID NUMBER ?????")
    print("! RESET FINISHED !")