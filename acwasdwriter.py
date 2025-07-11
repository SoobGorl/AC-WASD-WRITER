import time
import pyautogui
import letterpointers

# USE ONLY WHEN DOLPHIN CONTROLLER INPUT IS SET TO "STANDARD CONTROLLER" AND KEYBOARD STICK PRESSES ARE SET TO "WASD"

print("WAITING 10 SECONDS BEFORE INPUTTING KEYPRESSES! SWITCH TABS NOW!")
time.sleep(10)

# CHANGE DELAY IN LETTERPOINTERS. figure out how to put it here without it erroring (from letterpointers import key_delay)

# if esc pressed, stop all
# are you sure you want to continue? your message exceeds the letter character amount (255)
# FOR ME make sure to add space commands with trigger and also automatic line breaks for line-by-line stuff
# ALSO FOR ME if a word exceeds the linebreak try to cut it off early instead of splitting it in half
# TODO! BIND KEYS + ADD OTHER STUFF BESIDES LETTERS (NUMBERS, SYMBOLS, ETC). ADD PASTABLE TEXT AND CONVERT THAT TEXT INTO LETTER-BY-LETTER PARSING


# when a called, execute:
letterpointers.letter_a()
