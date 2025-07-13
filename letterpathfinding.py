import time
import pyautogui
import pydirectinput
from letters import *

key_delay = 0
# time between stick presses
letter_delay = 0
# time between letters

def up():
    time.sleep(key_delay)
    pydirectinput.press("w")
    print("W PRESS (1 / UP)")
def left():
    time.sleep(key_delay)
    pydirectinput.press("a")
    print("A PRESS (3 / LEFT)")
def down():
    time.sleep(key_delay)
    pydirectinput.press("s")
    print("S PRESS (2 / DOWN)")
def right():
    time.sleep(key_delay)
    pydirectinput.press("d")
    print("D PRESS (4 / RIGHT)")
def select():
    time.sleep(key_delay)
    pydirectinput.press("e")
    print("SELECTING " + letter_changer[0] + " (A PRESS)")
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

NULL = [0] # this is here because without it, running the script tries to ouput path_a immediately before anything else.

letter_trans(NULL or path_a or path_b or path_c or path_d or
           path_e or path_f or path_j or path_k or path_l or
           path_m or path_n or path_o or path_p or path_q or
           path_r or path_s or path_t or path_u or path_v or
           path_w or path_x or path_y or path_z)

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

rank_reset(NULL or path_a or path_b or path_c or path_d or
           path_e or path_f or path_j or path_k or path_l or
           path_m or path_n or path_o or path_p or path_q or
           path_r or path_s or path_t or path_u or path_v or
           path_w or path_x or path_y or path_z)