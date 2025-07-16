from key_pathfinding_math import *

# KEY COMMANDS
def command_space():
    time.sleep(key_delay)
    letter_changer[0] = "F"
    print("SELECTING " + letter_changer[0] + " (SPACE / LEFT TRIGGER)")
    pydirectinput.press("f")
    time.sleep(letter_delay)

# LETTERS
def letter_a():
    letter_changer[0] = "A"
    new_letter_printer()
    letter_trans(path_a)
    select()
    return rank_reset(path_a)
def letter_b():
    letter_changer[0] = "B"
    new_letter_printer()
    letter_trans(path_b)
    select()
    return rank_reset(path_b)
def letter_c():
    letter_changer[0] = "C"
    new_letter_printer()
    letter_trans(path_c)
    select()
    return rank_reset(path_c)
def letter_d():
    letter_changer[0] = "D"
    new_letter_printer()
    letter_trans(path_d)
    select()
    return rank_reset(path_d)
def letter_e():
    letter_changer[0] = "E"
    new_letter_printer()
    letter_trans(path_e)
    select()
    return rank_reset(path_e)
def letter_f():
    letter_changer[0] = "F"
    new_letter_printer()
    letter_trans(path_f)
    select()
    return rank_reset(path_f)
def letter_g():
    letter_changer[0] = "G"
    new_letter_printer()
    letter_trans(path_g)
    select()
    return rank_reset(path_g)
def letter_h():
    letter_changer[0] = "H"
    new_letter_printer()
    letter_trans(path_h)
    select()
    return rank_reset(path_h)
def letter_i():
    letter_changer[0] = "I"
    new_letter_printer()
    letter_trans(path_i)
    select()
    return rank_reset(path_i)
def letter_j():
    letter_changer[0] = "J"
    new_letter_printer()
    letter_trans(path_j)
    select()
    return rank_reset(path_j)
def letter_k():
    letter_changer[0] = "K"
    new_letter_printer()
    letter_trans(path_k)
    select()
    return rank_reset(path_k)
def letter_l():
    letter_changer[0] = "L"
    new_letter_printer()
    letter_trans(path_l)
    select()
    return rank_reset(path_l)
def letter_m():
    letter_changer[0] = "M"
    new_letter_printer()
    letter_trans(path_m)
    select()
    return rank_reset(path_m)
def letter_n():
    letter_changer[0] = "N"
    new_letter_printer()
    letter_trans(path_n)
    select()
    return rank_reset(path_n)
def letter_o():
    letter_changer[0] = "O"
    new_letter_printer()
    letter_trans(path_o)
    select()
    return rank_reset(path_o)
def letter_p():
    letter_changer[0] = "P"
    new_letter_printer()
    letter_trans(path_p)
    select()
    return rank_reset(path_p)
def letter_q():
    letter_changer[0] = "Q"
    new_letter_printer()
    letter_trans(path_q)
    select()
    return rank_reset(path_q)
def letter_r():
    letter_changer[0] = "R"
    new_letter_printer()
    letter_trans(path_r)
    select()
    return rank_reset(path_r)
def letter_s():
    letter_changer[0] = "S"
    new_letter_printer()
    letter_trans(path_s)
    select()
    return rank_reset(path_s)
def letter_t():
    letter_changer[0] = "T"
    new_letter_printer()
    letter_trans(path_t)
    select()
    return rank_reset(path_t)
def letter_u():
    letter_changer[0] = "U"
    new_letter_printer()
    letter_trans(path_u)
    select()
    return rank_reset(path_u)
def letter_v():
    letter_changer[0] = "V"
    new_letter_printer()
    letter_trans(path_v)
    select()
    return rank_reset(path_v)
def letter_w():
    letter_changer[0] = "W"
    new_letter_printer()
    letter_trans(path_w)
    select()
    return rank_reset(path_w)
def letter_x():
    letter_changer[0] = "X"
    new_letter_printer()
    letter_trans(path_x)
    select()
    return rank_reset(path_x)
def letter_y():
    letter_changer[0] = "Y"
    new_letter_printer()
    letter_trans(path_y)
    select()
    return rank_reset(path_y)
def letter_z():
    letter_changer[0] = "Z"
    new_letter_printer()
    letter_trans(path_z)
    select()
    return rank_reset(path_z)

# KEY CODES
def keycode_return():
    letter_changer[0] = "RETURN"
    new_letter_printer()
    letter_trans(path_return)
    select()
    return rank_reset(path_return)

# NUMBERS
def number_one():
    letter_changer[0] = "1"
    new_letter_printer()
    caps_toggle()
    letter_trans(path_one)
    select()
    rank_reset(path_one)
    return caps_toggle()
def number_two():
    letter_changer[0] = "2"
    new_letter_printer()
    caps_toggle()
    letter_trans(path_two)
    select()
    rank_reset(path_two)
    return caps_toggle()
def number_three():
    letter_changer[0] = "3"
    new_letter_printer()
    caps_toggle()
    letter_trans(path_three)
    select()
    rank_reset(path_three)
    return caps_toggle()
def number_four():
    letter_changer[0] = "4"
    new_letter_printer()
    caps_toggle()
    letter_trans(path_four)
    select()
    rank_reset(path_four)
    return caps_toggle()
def number_five():
    letter_changer[0] = "5"
    new_letter_printer()
    caps_toggle()
    letter_trans(path_five)
    select()
    rank_reset(path_five)
    return caps_toggle()
def number_six():
    letter_changer[0] = "6"
    new_letter_printer()
    caps_toggle()
    letter_trans(path_six)
    select()
    rank_reset(path_six)
    return caps_toggle()
def number_seven():
    letter_changer[0] = "7"
    new_letter_printer()
    caps_toggle()
    letter_trans(path_seven)
    select()
    rank_reset(path_seven)
    return caps_toggle()
def number_eight():
    letter_changer[0] = "8"
    new_letter_printer()
    caps_toggle()
    letter_trans(path_eight)
    select()
    rank_reset(path_eight)
    return caps_toggle()
def number_nine():
    letter_changer[0] = "9"
    new_letter_printer()
    caps_toggle()
    letter_trans(path_nine)
    select()
    rank_reset(path_nine)
    return caps_toggle()
def number_zero():
    letter_changer[0] = "0"
    new_letter_printer()
    caps_toggle()
    letter_trans(path_zero)
    select()
    rank_reset(path_zero)
    return caps_toggle()

# FAILED CAPITAL TOGGLER
#def caps_toggle():
    #pydirectinput.press("g")
#caps = True
#if caps:
    #caps_toggle()
    #print("!!! CAPS TOGGLE !!!")
    #select()
    #caps_toggle()
    # set caps to false?
#else:
    #select()
    #print("### NO CAPS ###")