import time
from key_functions import *
import sys

# TODO! if esc pressed, stop all
# fix transparency issues in logo/icon? make colors pop more
# 192 potential characters in letter, 32 per line. some characters reduce letter count

# TODO! for each letter that is capitalized, run a command that makes the game capitalize all for that letter
# TODO!!!! like caps = true, make it caps, select value, then make it not caps and then set it to false
# TODO! add debug mode (shows "W PRESS" and everything else. non-debug only shows "pressing A" when targeting)

# TODO DEBUG
# shows text string + wasd presses
# TODO CAPS

version_number = "1.1.3"
devnumber = "1.1.3#5"

def sleepy_time():
    time.sleep(8) # 8 second break, for alt tabbing
def pause_break():
    time.sleep(0) # (whatever) second break, for short pauses. unused because artificial pauses = bad for testing!!

def speed_slow():
    pydirectinput.PAUSE = 0.050
def speed_normal():
    pydirectinput.PAUSE = 0.035
def speed_fast():
    pydirectinput.PAUSE = 0.017

tab_presser = False

print("ACWASD VERSION " + version_number + "\n")
print("MAKE SURE YOU ARE IN QWERTY MODE, IN ALL LOWERCASE, AND CURSOR IS ON THE \"!\" KEY.\n")
print("VALID KEYCODES: ! ? \" ' ; : , . - ~")
print("NUMBERS ARE ALLOWED! :)")
print("CAPITALIZATION IS >NOT< ALLOWED... :(\n")
pause_break()

while True:
    init_troubleshooter = input("Pick between SLOW, NORMAL, or FAST: ")
    if init_troubleshooter.lower() in ["s", "slow", "slower"]:
        print("Time between inputs will be slower (0.050).")
        # " + str(speed_slow) + "
        speed_slow()
        tab_presser = False # to make sure it's STILL false incase anything goes wrong.
        pause_break()
        break
    elif init_troubleshooter.lower() in ["n", "normal", "medium"]:
        print("Time between inputs will be normal (0.035).")
        # " + str(speed_normal) + "
        speed_normal()
        tab_presser = False # same as in "slow"
        pause_break()
        break
    elif init_troubleshooter.lower() in ["f", "fast", "faster"]:
        print("Time between inputs will be faster (0.017).")
        # " + str(speed_fast) + "
        speed_fast()
        tab_presser = True
        pause_break()
        break
    else:
        print("That speed does not exist.")

text_input = input("Please input your desired text here: ")
text_list = list(text_input)

# print(text_list)
# shows inputted text as a list, separated like ['t', 'h', 'i', 's', ' ', '!']. useful for debugging if enabled.

def input_transcriber():
    for key_input in text_list:
        if key_input == "a":
            letter_a()
            #if key_input == "A":
                #letter_a(caps)
        elif key_input == "b":
            letter_b()
        elif key_input == "c":
            letter_c()
        elif key_input == "d":
            letter_d()
        elif key_input == "e":
            letter_e()
        elif key_input == "f":
            letter_f()
        elif key_input == "g":
            letter_g()
        elif key_input == "h":
            letter_h()
        elif key_input == "i":
            letter_i()
        elif key_input == "j":
            letter_j()
        elif key_input == "k":
            letter_k()
        elif key_input == "l":
            letter_l()
        elif key_input == "m":
            letter_m()
        elif key_input == "n":
            letter_n()
        elif key_input == "o":
            letter_o()
        elif key_input == "p":
            letter_p()
        elif key_input == "q":
            letter_q()
        elif key_input == "r":
            letter_r()
        elif key_input == "s":
            letter_s()
        elif key_input == "t":
            letter_t()
        elif key_input == "u":
            letter_u()
        elif key_input == "v":
            letter_v()
        elif key_input == "w":
            letter_w()
        elif key_input == "x":
            letter_x()
        elif key_input == "y":
            letter_y()
        elif key_input == "z":
            letter_z()
        elif key_input == " ":
            command_space()
        elif key_input == "1":
            number_one()
        elif key_input == "2":
            number_two()
        elif key_input == "3":
            number_three()
        elif key_input == "4":
            number_four()
        elif key_input == "5":
            number_five()
        elif key_input == "6":
            number_six()
        elif key_input == "7":
            number_seven()
        elif key_input == "8":
            number_eight()
        elif key_input == "9":
            number_nine()
        elif key_input == "0":
            number_zero()
        elif key_input == "!":
            keycode_exclamationmark()
        elif key_input == "?":
            keycode_questionmark()
        elif key_input == '"':
            keycode_quotationmark()
        elif key_input == "-":
            keycode_dash()
        elif key_input == "~":
            keycode_tilde()
        #elif key_input == "&DASH":
            #keycode_doubledash()
        elif key_input == "'":
            keycode_apostrophe()
        elif key_input == ";":
            keycode_semicolon()
        elif key_input == ":":
            keycode_colon()
        #elif key_input == "&KEY":
            #keycode_key()
        #elif key_input == "&RETURN":
            #keycode_return()
        elif key_input == ",":
            keycode_comma()
        elif key_input == ".":
            keycode_period()
        else:
            print("If you're seeing this, a failsafe failed. Oops!")
            print("You probably inputted an invalid keycode.")
            print("Please use ONLY LOWERCASE letters and BASIC punctuation.")
            print("Program will close in 8 seconds.")
            sleepy_time()
            sys.exit("PROGRAM CLOSED DUE TO AN UNKNOWN ERROR.")

print("SWITCH TABS NOW! WAITING 8 SECONDS BEFORE INPUTTING KEYPRESSES!")
sleepy_time()

if tab_presser: # holds down TAB if in fast mode
    pydirectinput.keyDown("tab")
else:
    pass

input_transcriber() # executes typed text as controller inputs

if tab_presser: # releases TAB if in fast mode
    pydirectinput.keyUp("tab")
else:
    pass

print("PROGRAM COMPLETE. WAITING 8 SECONDS BEFORE CLOSING.")
sleepy_time()
sys.exit("PROGRAM TERMINATED.")

# i was going to implement this but nah, waiting until v2
valid_keys = ["a", "b", "c", "d", "e", "f", "g", "h", "i",
              "j", "k", "l", "m", "n", "o", "p", "q", "r",
              "s", "t", "u", "v", "w", "x", "y", "z", " ",
              "1", "2", "3", "4", "5", "6", "7", "8", "9",
              "0"]
if text_input not in valid_keys:
    print("!!! AT LEAST ONE INVALID INPUT !!!")
    list_comparer = set(text_input).difference(set(valid_keys))
    print(f"OFFENDING KEY CODES: " + str(list_comparer))
    print("Please use only LOWERCASE letters!") #, numbers, and BASIC punctuation
    print("Program will close by itself in 8 seconds.")
    sleepy_time()
    sys.exit("PROGRAM CLOSED DUE TO AN INVALID KEY CODE.")