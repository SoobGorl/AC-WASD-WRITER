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

def letter_a():
    letter_changer[0] = "A"
    print("TARGETING " + letter_changer[0])
    down(), down()
    return select()
def letter_b():
    letter_changer[0] = "B"
    print("TARGETING " + letter_changer[0])
    down(), down(), down(), right(), right(), right(), right()
    return select()
def letter_c():
    letter_changer[0] = "C"
    print("TARGETING " + letter_changer[0])
    down(), down(), down(), right(), right()
    return select()
def letter_d():
    letter_changer[0] = "D"
    print("TARGETING " + letter_changer[0])
    down(), down(), right(), right()
    return select()
def letter_e():
    letter_changer[0] = "E"
    print("TARGETING " + letter_changer[0])
    down(), right(), right()
    return select()
def letter_f():
    letter_changer[0] = "F"
    print("TARGETING " + letter_changer[0])
    down(), down(), right(), right(), right()
    return select()
def letter_g():
    letter_changer[0] = "G"
    print("TARGETING " + letter_changer[0])
    down(), down(), right(), right(), right(), right()
    return select()
def letter_h():
    letter_changer[0] = "H"
    print("TARGETING " + letter_changer[0])
    down(), down(), right(), right(), right(), right(), right()
    return select()
def letter_i():
    letter_changer[0] = "I"
    print("TARGETING " + letter_changer[0])
    down(), right(), right(), right(), right(), right(), right(), right()
    return select()
def letter_j():
    letter_changer[0] = "J"
    print("TARGETING " + letter_changer[0])
    down(), down(), right(), right(), right(), right(), right(), right()
    return select()
def letter_k():
    letter_changer[0] = "K"
    print("TARGETING " + letter_changer[0])
    down(), down(), right(), right(), right(), right(), right(), right(), right()
    return select()
def letter_l():
    letter_changer[0] = "L"
    print("TARGETING " + letter_changer[0])
    down(), down(), right(), right(), right(), right(), right(), right(), right(), right()
    return select()
def letter_m():
    letter_changer[0] = "M"
    print("TARGETING " + letter_changer[0])
    down(), down(), down(), right(), right(), right(), right(), right(), right()
    return select()
def letter_n():
    letter_changer[0] = "N"
    print("TARGETING " + letter_changer[0])
    down(), down(), down(), right(), right(), right(), right(), right()
    return select()
def letter_o():
    letter_changer[0] = "O"
    print("TARGETING " + letter_changer[0])
    down(), right(), right(), right(), right(), right(), right(), right(), right()
    return select()
def letter_p():
    letter_changer[0] = "P"
    print("TARGETING " + letter_changer[0])
    down(), right(), right(), right(), right(), right(), right(), right(), right(), right()
    return select()
def letter_q():
    letter_changer[0] = "Q"
    print("TARGETING " + letter_changer[0])
    down()
    return select()
def letter_r():
    letter_changer[0] = "R"
    print("TARGETING " + letter_changer[0])
    down(), right(), right(), right()
    return select()
def letter_s():
    letter_changer[0] = "S"
    print("TARGETING " + letter_changer[0])
    down(), down(), right()
    return select()
def letter_t():
    letter_changer[0] = "T"
    print("TARGETING " + letter_changer[0])
    down(), right(), right(), right(), right()
    return select()
def letter_u():
    letter_changer[0] = "U"
    print("TARGETING " + letter_changer[0])
    down(), right(), right(), right(), right(), right(), right()
    return select()
def letter_v():
    letter_changer[0] = "V"
    print("TARGETING " + letter_changer[0])
    down(), down(), down(), right(), right(), right()
    return select()
def letter_w():
    letter_changer[0] = "W"
    print("TARGETING " + letter_changer[0])
    down(), right()
    return select()
def letter_x():
    letter_changer[0] = "X"
    print("TARGETING " + letter_changer[0])
    down(), down(), down(), right()
    return select()
def letter_y():
    letter_changer[0] = "Y"
    print_new_letter()
    down(), right(), right(), right(), right(), right()
    return select()
def letter_z():
    letter_changer[0] = "Z"
    print("TARGETING " + letter_changer[0])
    down(), down(), down()
    return select()

letter_a(), letter_b(), letter_c(), letter_d(), letter_e(), letter_f(), letter_g(), letter_h(), letter_i()
letter_j(), letter_k(), letter_l(), letter_m(), letter_n(), letter_o(), letter_p(), letter_q(), letter_r(),
letter_s(), letter_t(), letter_u(), letter_v(), letter_w(), letter_x(), letter_y(), letter_z()


#target = "TARGETING" + letter_changer[0]

