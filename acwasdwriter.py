import time
from letterpointers import *

# USE ONLY WHEN DOLPHIN CONTROLLER INPUT IS SET TO "STANDARD CONTROLLER" AND KEYBOARD STICK PRESSES ARE SET TO
# "WASD" (E IS SELECT, Q IS SPACE, R IS CYCLE THROUGH SYMBOLS AND STUFF)

print("WAITING 3 SECONDS BEFORE INPUTTING KEYPRESSES! SWITCH TABS NOW!")
time.sleep(3)
# sleepy_time = time.sleep(3)

# if esc pressed, stop all
# are you sure you want to continue? your message exceeds the letter character amount (255)
# FOR ME make sure to add space commands with trigger and also automatic line breaks for line-by-line stuff
# ALSO FOR ME if a word exceeds the linebreak try to cut it off early instead of splitting it in half
# TODO! BIND KEYS + ADD OTHER STUFF BESIDES LETTERS (NUMBERS, SYMBOLS, ETC). ADD PASTABLE TEXT AND CONVERT THAT TEXT INTO LETTER-BY-LETTER PARSING

# text commands
#letter_a(), letter_b(), letter_c(), letter_d(), letter_e(), letter_f(), letter_g(), letter_h(), letter_i()
#letter_j(), letter_k(), letter_l(), letter_m(), letter_n(), letter_o(), letter_p(), letter_q(), letter_r(),
#letter_s(), letter_t(), letter_u(), letter_v(), letter_w(), letter_x(), letter_y(), letter_z()

#letter_b(), letter_o(), letter_w(), letter_l(), letter_i(), letter_n(), letter_g()

letter_a(), letter_b(), letter_c(), letter_d(), letter_e()
text_input = input("")

text_list = list(text_input)

print(text_list)

#print("PROGRAM FINISHED. WAITING 3 SECONDS.")
#time.sleep(3)

# PRINTING TEST STRING
# DID THIS OUTPUT "BOWLING!" ?
# Y / N
# SETTINGS HAVE BEEN CHANGED. TRY AGAIN IN 5 SECONDS.