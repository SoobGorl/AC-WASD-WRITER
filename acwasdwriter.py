import time
from letterpointers import *
import sys

# potential speed-up but making game speed faster for more inputs? script has to not be slow first though lol

# 192 potential characters in letter, 32 per line

def sleepy_time():
    time.sleep(8) # 8 second break, for alt tabbing
def pause_break():
    time.sleep(0) # (whatever) second break, for short pauses. maybe 1.

# TODO! hold down tab when keycodes start executing, release tab when string over

# TODO! add 3 speed options in the beginning:
# TODO! 0.035 for normal speed (30fps) 0.17 for 2x speed (60 fps, milage varies), and 0.05 for slow mode (bad pc :cc)

print("MAKE SURE YOU ARE IN QWERTY MODE, IN ALL LOWERCASE.")
pause_break()

while True: # if no, run through things individually to see if it's better.
    init_troubleshooter = input("Start with troubleshooting? (Y/N): ")
    if init_troubleshooter.lower() in ["n", "no"]:
        print("Continuing with program.")
        pause_break()
        break
    elif init_troubleshooter.lower() in ["y", "yes"]:
        print("Proceeding with troubleshooter.")
        print("SWITCH TABS NOW! WAITING 8 SECONDS BEFORE INPUTTING KEYPRESSES!")
        sleepy_time()  # program-wide "pause period"
        print("PRINTING TEST PATTERN.")
        test_pattern()
        while True:
            init_userqa = input("DID THIS OUTPUT \"BOWLING\" ? (Y/N): ")
            if init_userqa.lower() in ["n", "no"]: # TODO! if no, run through things individually to see if that fixes things.
                print("Potential fixes have been made. Change nothing in-game. Make sure you are on \"letters.\"")
                key_delay = 0.5
                # layout_abcdef = True TODO! set initial command in text string to toggling abcdef keyboard
                # cursor_aligner = True TODO! set initial command in text string to set cursor to top left at exclaimation mark
                pause_break()
                break
            elif init_userqa.lower() in ["y" or "yes"]:
                print("Continuing with program.")
                pause_break()
                break
            else:
                print("Please type \"Y\" or \"N\".")
        pause_break()
        break
    else:
        print("Please type \"Y\" or \"N\".")

text_input = input("Please input your desired text here: ")
text_list = list(text_input)
print(text_list)

print("SWITCH TABS NOW! WAITING 8 SECONDS BEFORE INPUTTING KEYPRESSES!")
sleepy_time()

def input_transcriber():
    for key_input in text_list:
        if key_input == "a":
            letter_a()
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
        else:
            sys.exit(f"!!! INVALID KEY: {key_input} !!!")

input_transcriber()

# if word exceeds 32 character limit then on previous word run keycode_return()

print("PROGRAM COMPLETE. WAITING 8 SECONDS BEFORE CLOSING.")
sleepy_time()

# TEST STRINGS
# letter_a(), letter_b(), letter_c(), letter_d(), letter_e(), letter_f(), letter_g(), letter_h(), letter_i()
# letter_j(), letter_k(), letter_l(), letter_m(), letter_n(), letter_o(), letter_p(), letter_q(), letter_r(),
# letter_s(), letter_t(), letter_u(), letter_v(), letter_w(), letter_x(), letter_y(), letter_z()

# USE ONLY WHEN DOLPHIN CONTROLLER INPUT IS SET TO "STANDARD CONTROLLER" AND KEYBOARD STICK PRESSES ARE SET TO
# "WASD" (E IS SELECT, Q IS SPACE, R IS CYCLE THROUGH SYMBOLS AND STUFF)
# TODO! if esc pressed, stop all
# TODO! are you sure you want to continue? your message exceeds the letter character amount (255)
# TODO! FOR ME make sure to add space commands with trigger and also automatic line breaks for line-by-line stuff
# TODO! ALSO FOR ME if a word exceeds the linebreak try to cut it off early instead of splitting it in half
# TODO! BIND KEYS + ADD OTHER STUFF BESIDES LETTERS (NUMBERS, SYMBOLS, ETC). ADD PASTABLE TEXT AND CONVERT THAT TEXT INTO LETTER-BY-LETTER PARSING