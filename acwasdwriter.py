import time
from letterpointers import *

def sleepy_time():
    time.sleep(8) # 8 second break, for alt tabbing
def pause_break():
    time.sleep(2) # 2 second break, for short pauses

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

text_input = input("Please input your text here: ")






#letter_a(), letter_b(), letter_c(), letter_d(), letter_e(), letter_f(), letter_g(), letter_h(), letter_i()
#letter_j(), letter_k(), letter_l(), letter_m(), letter_n(), letter_o(), letter_p(), letter_q(), letter_r(),
#letter_s(), letter_t(), letter_u(), letter_v(), letter_w(), letter_x(), letter_y(), letter_z()





#text_list = list(text_input)
#print(text_list)

#print("PROGRAM FINISHED. WAITING 3 SECONDS.")
#sleepy_time()

# SETTINGS HAVE BEEN CHANGED. TRY AGAIN IN 5 SECONDS (this will make it so that key_delay = 1 instead of 0)
# yes (sets key_day to 1) no (sets key_delay to 0)

# USE ONLY WHEN DOLPHIN CONTROLLER INPUT IS SET TO "STANDARD CONTROLLER" AND KEYBOARD STICK PRESSES ARE SET TO
# "WASD" (E IS SELECT, Q IS SPACE, R IS CYCLE THROUGH SYMBOLS AND STUFF)
# TODO! if esc pressed, stop all
# TODO! are you sure you want to continue? your message exceeds the letter character amount (255)
# TODO! FOR ME make sure to add space commands with trigger and also automatic line breaks for line-by-line stuff
# TODO! ALSO FOR ME if a word exceeds the linebreak try to cut it off early instead of splitting it in half
# TODO! BIND KEYS + ADD OTHER STUFF BESIDES LETTERS (NUMBERS, SYMBOLS, ETC). ADD PASTABLE TEXT AND CONVERT THAT TEXT INTO LETTER-BY-LETTER PARSING