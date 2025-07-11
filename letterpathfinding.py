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
def rank_reset_a():
    print("! RESET !")
    rank_reverser = list(map(lambda x: x - 1, path_a))
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
    print("! RESET FINISHED !")

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
def rank_reset_b():
    print("! RESET !")
    rank_reverser = list(map(lambda x: x - 1, path_b))
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
    print("! RESET FINISHED !")

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
def rank_reset_c():
    print("! RESET !")
    rank_reverser = list(map(lambda x: x - 1, path_c))
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
    print("! RESET FINISHED !")

def letter_trans_d():
    for lister_func in path_d:
        if lister_func == 1:
            up()
        elif lister_func == 2:
            down()
        elif lister_func == 3:
            left()
        elif lister_func == 4:
            right()
def rank_reset_d():
    print("! RESET !")
    rank_reverser = list(map(lambda x: x - 1, path_d))
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
    print("! RESET FINISHED !")

def letter_trans_e():
    for lister_func in path_e:
        if lister_func == 1:
            up()
        elif lister_func == 2:
            down()
        elif lister_func == 3:
            left()
        elif lister_func == 4:
            right()
def rank_reset_e():
    print("! RESET !")
    rank_reverser = list(map(lambda x: x - 1, path_e))
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
    print("! RESET FINISHED !")

def letter_trans_f():
    for lister_func in path_f:
        if lister_func == 1:
            up()
        elif lister_func == 2:
            down()
        elif lister_func == 3:
            left()
        elif lister_func == 4:
            right()
def rank_reset_f():
    print("! RESET !")
    rank_reverser = list(map(lambda x: x - 1, path_f))
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
    print("! RESET FINISHED !")

def letter_trans_g():
    for lister_func in path_g:
        if lister_func == 1:
            up()
        elif lister_func == 2:
            down()
        elif lister_func == 3:
            left()
        elif lister_func == 4:
            right()
def rank_reset_g():
    print("! RESET !")
    rank_reverser = list(map(lambda x: x - 1, path_g))
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
    print("! RESET FINISHED !")

def letter_trans_h():
    for lister_func in path_h:
        if lister_func == 1:
            up()
        elif lister_func == 2:
            down()
        elif lister_func == 3:
            left()
        elif lister_func == 4:
            right()
def rank_reset_h():
    print("! RESET !")
    rank_reverser = list(map(lambda x: x - 1, path_h))
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
    print("! RESET FINISHED !")

def letter_trans_i():
    for lister_func in path_i:
        if lister_func == 1:
            up()
        elif lister_func == 2:
            down()
        elif lister_func == 3:
            left()
        elif lister_func == 4:
            right()
def rank_reset_i():
    print("! RESET !")
    rank_reverser = list(map(lambda x: x - 1, path_i))
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
    print("! RESET FINISHED !")

def letter_trans_j():
    for lister_func in path_j:
        if lister_func == 1:
            up()
        elif lister_func == 2:
            down()
        elif lister_func == 3:
            left()
        elif lister_func == 4:
            right()
def rank_reset_j():
    print("! RESET !")
    rank_reverser = list(map(lambda x: x - 1, path_j))
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
    print("! RESET FINISHED !")

def letter_trans_k():
    for lister_func in path_k:
        if lister_func == 1:
            up()
        elif lister_func == 2:
            down()
        elif lister_func == 3:
            left()
        elif lister_func == 4:
            right()
def rank_reset_k():
    print("! RESET !")
    rank_reverser = list(map(lambda x: x - 1, path_k))
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
    print("! RESET FINISHED !")

def letter_trans_l():
    for lister_func in path_l:
        if lister_func == 1:
            up()
        elif lister_func == 2:
            down()
        elif lister_func == 3:
            left()
        elif lister_func == 4:
            right()
def rank_reset_l():
    print("! RESET !")
    rank_reverser = list(map(lambda x: x - 1, path_l))
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
    print("! RESET FINISHED !")

def letter_trans_m():
    for lister_func in path_m:
        if lister_func == 1:
            up()
        elif lister_func == 2:
            down()
        elif lister_func == 3:
            left()
        elif lister_func == 4:
            right()
def rank_reset_m():
    print("! RESET !")
    rank_reverser = list(map(lambda x: x - 1, path_m))
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
    print("! RESET FINISHED !")

def letter_trans_n():
    for lister_func in path_n:
        if lister_func == 1:
            up()
        elif lister_func == 2:
            down()
        elif lister_func == 3:
            left()
        elif lister_func == 4:
            right()
def rank_reset_n():
    print("! RESET !")
    rank_reverser = list(map(lambda x: x - 1, path_n))
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
    print("! RESET FINISHED !")

def letter_trans_o():
    for lister_func in path_o:
        if lister_func == 1:
            up()
        elif lister_func == 2:
            down()
        elif lister_func == 3:
            left()
        elif lister_func == 4:
            right()
def rank_reset_o():
    print("! RESET !")
    rank_reverser = list(map(lambda x: x - 1, path_o))
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
    print("! RESET FINISHED !")

def letter_trans_p():
    for lister_func in path_p:
        if lister_func == 1:
            up()
        elif lister_func == 2:
            down()
        elif lister_func == 3:
            left()
        elif lister_func == 4:
            right()
def rank_reset_p():
    print("! RESET !")
    rank_reverser = list(map(lambda x: x - 1, path_p))
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
    print("! RESET FINISHED !")

def letter_trans_q():
    for lister_func in path_q:
        if lister_func == 1:
            up()
        elif lister_func == 2:
            down()
        elif lister_func == 3:
            left()
        elif lister_func == 4:
            right()
def rank_reset_q():
    print("! RESET !")
    rank_reverser = list(map(lambda x: x - 1, path_q))
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
    print("! RESET FINISHED !")

def letter_trans_r():
    for lister_func in path_r:
        if lister_func == 1:
            up()
        elif lister_func == 2:
            down()
        elif lister_func == 3:
            left()
        elif lister_func == 4:
            right()
def rank_reset_r():
    print("! RESET !")
    rank_reverser = list(map(lambda x: x - 1, path_r))
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
    print("! RESET FINISHED !")

def letter_trans_s():
    for lister_func in path_s:
        if lister_func == 1:
            up()
        elif lister_func == 2:
            down()
        elif lister_func == 3:
            left()
        elif lister_func == 4:
            right()
def rank_reset_s():
    print("! RESET !")
    rank_reverser = list(map(lambda x: x - 1, path_s))
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
    print("! RESET FINISHED !")

def letter_trans_t():
    for lister_func in path_t:
        if lister_func == 1:
            up()
        elif lister_func == 2:
            down()
        elif lister_func == 3:
            left()
        elif lister_func == 4:
            right()
def rank_reset_t():
    print("! RESET !")
    rank_reverser = list(map(lambda x: x - 1, path_t))
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
    print("! RESET FINISHED !")

def letter_trans_u():
    for lister_func in path_u:
        if lister_func == 1:
            up()
        elif lister_func == 2:
            down()
        elif lister_func == 3:
            left()
        elif lister_func == 4:
            right()
def rank_reset_u():
    print("! RESET !")
    rank_reverser = list(map(lambda x: x - 1, path_u))
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
    print("! RESET FINISHED !")

def letter_trans_v():
    for lister_func in path_v:
        if lister_func == 1:
            up()
        elif lister_func == 2:
            down()
        elif lister_func == 3:
            left()
        elif lister_func == 4:
            right()
def rank_reset_v():
    print("! RESET !")
    rank_reverser = list(map(lambda x: x - 1, path_v))
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
    print("! RESET FINISHED !")

def letter_trans_w():
    for lister_func in path_w:
        if lister_func == 1:
            up()
        elif lister_func == 2:
            down()
        elif lister_func == 3:
            left()
        elif lister_func == 4:
            right()
def rank_reset_w():
    print("! RESET !")
    rank_reverser = list(map(lambda x: x - 1, path_w))
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
    print("! RESET FINISHED !")

def letter_trans_x():
    for lister_func in path_x:
        if lister_func == 1:
            up()
        elif lister_func == 2:
            down()
        elif lister_func == 3:
            left()
        elif lister_func == 4:
            right()
def rank_reset_x():
    print("! RESET !")
    rank_reverser = list(map(lambda x: x - 1, path_x))
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
    print("! RESET FINISHED !")

def letter_trans_y():
    for lister_func in path_y:
        if lister_func == 1:
            up()
        elif lister_func == 2:
            down()
        elif lister_func == 3:
            left()
        elif lister_func == 4:
            right()
def rank_reset_y():
    print("! RESET !")
    rank_reverser = list(map(lambda x: x - 1, path_y))
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
    print("! RESET FINISHED !")

def letter_trans_z():
    for lister_func in path_z:
        if lister_func == 1:
            up()
        elif lister_func == 2:
            down()
        elif lister_func == 3:
            left()
        elif lister_func == 4:
            right()
def rank_reset_z():
    print("! RESET !")
    rank_reverser = list(map(lambda x: x - 1, path_z))
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
    print("! RESET FINISHED !")