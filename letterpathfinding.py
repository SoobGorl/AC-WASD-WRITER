import time
import pyautogui
key_delay = 0.2
# time between stick presses
letter_delay = 0.5
# time between letters

def up():
    time.sleep(key_delay)
    pyautogui.press("w")
    print("W PRESS (UP)")
    # ADD 1 TO "UP_NUMBER" increment it by 1, for math stuff in the future
def left():
    time.sleep(key_delay)
    pyautogui.press("a")
    print("A PRESS (LEFT)")
def down():
    time.sleep(key_delay)
    pyautogui.press("s")
    print("S PRESS (DOWN)")
def right():
    time.sleep(key_delay)
    pyautogui.press("d")
    print("D PRESS (RIGHT)")
def select():
    time.sleep(key_delay)
    pyautogui.press("e")
    print("SELECTING " + letter_changer[0] + " (A PRESS)")
    time.sleep(letter_delay)

letter_changer = ["NULL"]
def print_new_letter():
    print("TARGETING " + letter_changer[0])

def path_a():
    down(), down()
def path_b():
    down(), down(), down(), right(), right(), right(), right()
def path_c():
    down(), down(), down(), right(), right()
def path_d():
    down(), down(), right(), right()
def path_e():
    down(), right(), right()
def path_f():
    down(), down(), right(), right(), right()
def path_g():
    down(), down(), right(), right(), right(), right()
def path_h():
    down(), down(), right(), right(), right(), right(), right()
def path_i():
    down(), right(), right(), right(), right(), right(), right(), right()
def path_j():
    down(), down(), right(), right(), right(), right(), right(), right()
def path_k():
    down(), down(), right(), right(), right(), right(), right(), right(), right()
def path_l():
    down(), down(), right(), right(), right(), right(), right(), right(), right(), right()
def path_m():
    down(), down(), down(), right(), right(), right(), right(), right(), right()
def path_n():
    down(), down(), down(), right(), right(), right(), right(), right()
def path_o():
    down(), right(), right(), right(), right(), right(), right(), right(), right()
def path_p():
    down(), right(), right(), right(), right(), right(), right(), right(), right(), right()
def path_q():
    down()
def path_r():
    down(), right(), right(), right()
def path_s():
    down(), down(), right()
def path_t():
    down(), right(), right(), right(), right()
def path_u():
    down(), right(), right(), right(), right(), right(), right()
def path_v():
    down(), down(), down(), right(), right(), right()
def path_w():
    down(), right()
def path_x():
    down(), down(), down(), right()
def path_y():
    down(), right(), right(), right(), right(), right()
def path_z():
    down(), down(), down()