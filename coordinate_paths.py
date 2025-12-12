letters_qwerty = {
    # ROW 3
    "!": (0, 3),
    "?": (1, 3),
    "\"": (2, 3),
    "-": (3, 3),
    "~": (4, 3),
    "$LONGDASH$": (5,3 ),
    "\'": (6, 3),
    ";": (7, 3),
    ":": (8, 3),
    "$KEY$": (9, 3),
    # ROW 2
    "q": (0, 2),
    "w": (1, 2),
    "e": (2, 2),
    "r": (3, 2),
    "t": (4, 2),
    "y": (5, 2),
    "u": (6, 2),
    "i": (7, 2),
    "o": (8, 2),
    "p": (9, 2),
    # ROW 1
    "a": (0, 1),
    "s": (1, 1),
    "d": (2, 1),
    "f": (3, 1),
    "g": (4, 1),
    "h": (5, 1),
    "j": (6, 1),
    "k": (7, 1),
    "l": (8, 1),
    "$ENTER$": (9, 1),
    # ROW 0
    "z": (0, 0),
    "x": (1, 0),
    "c": (2, 0),
    "v": (3, 0),
    "b": (4, 0),
    "n": (5, 0),
    "m": (6, 0),
    ",": (7, 0),
    ".": (8, 0),
    "$SPACE$": (9, 0),
}

letters_upper = {
    # ROW 3
    "1": (0, 3),
    "2": (1, 3),
    "3": (2, 3),
    "4": (3, 3),
    "5": (4, 3),
    "6": (5, 3),
    "7": (6, 3),
    "8": (7, 3),
    "9": (8, 3),
    "0": (9, 3),
}

# figure out how to differenciate between these, do I just copy the other rows into here? might be good for sanity sake
letters_asdf = {
    # ROW 3
    "$DOT$": (9,3),
    # ROW 2
    "a": (0, 2),
    "b": (1, 2),
    "c": (2, 2),
    "d": (3, 2),
    "e": (4, 2),
    "f": (5, 2),
    "g": (6, 2),
    "h": (7, 2),
    "i": (8, 2),
    "j": (9, 2),
    # ROW 1
    "k": (0, 1),
    "l": (1, 1),
    "m": (2, 1),
    "n": (3, 1),
    "o": (4, 1),
    "p": (5, 1),
    "q": (6, 1),
    "r": (7, 1),
    "s": (8, 1),
    "$ENTER$": (9, 1), # duplicated
    # ROW 0
    "t": (0, 0),
    "u": (1, 0),
    "v": (2, 0),
    "w": (3, 0),
    "x": (4, 0),
    "y": (5, 0),
    "z": (6, 0),
    ",": (7, 0), # duplicated
    ".": (8, 0), # duplicated
    "$SPACE$": (9, 0) # duplicated
}

punct = {
    # ROW 3
    "#": (0, 3),
    "?": (1, 3), # duplicated
    "\"": (2, 3), # duplicated
    "-": (3, 3), # duplicated
    "$": (4, 3), # duplicated
    "$LONGDASH$": (5, 3), # duplicated
    "7": (6, 3), # duplicated
    "8": (7, 3), # duplicated
    "9": (8, 3), # duplicated
    "$AE$": (9, 3),
    # ROW 2
    "%": (0, 2),
    "&": (1, 2),
    "@": (2, 2),
    "_": (3, 2),
    "‾": (4, 2),
    "/": (5, 2),
    "¦": (6, 2), # its like a thick colon
    "$MULTIPLICATION$": (7, 2),
    "÷": (8, 2),
    "=": (9, 2),
    # ROW 1
    "(": (0, 1),
    ")": (1, 1),
    "<": (2, 1),
    ">": (3, 1),
    "$LESSTHANSTACK$": (4, 1),
    "$MORETHANSTACK$": (5, 1),
    "⚞": (6, 1),
    "⚟": (7, 1),
    "+": (8, 1),
    "$ENTER$": (9, 1),  # duplicated
    # ROW 0
    "β": (0, 0),
    "þ": (1, 0),
    "ð": (2, 0),
    "§": (3, 0),
    "$DOUBLELINEVERTICAL$": (4, 0),
    "μ": (5, 0),
    "¬": (6, 0),
    ",": (7, 0),  # duplicated
    ".": (8, 0),  # duplicated
    "$SPACE$": (9, 0)  # duplicated
}

# credits to https://sheet.shiar.nl/keyboard/altgr/animal, helped with tracking down unicode for these + punct
icons = {
    # ROW 3
    "♥": (0, 3), # MANY HEARTS, ACCOUNT FOR ALL OF THEM!!! SAME GOES FOR A LOT OF THESE ICONS!
    "★": (1, 3),
    "♪": (2, 3),
    "💧": (3, 3),
    "💢": (4, 3),
    "❀": (5, 3), #
    "🐾": (6, 3),
    "♂": (7, 3),
    "♀": (8, 3),
    "∞": (9, 3),
    # ROW 2
    "○": (0, 2), #
    "☓": (1, 2), # XX
    "□": (2, 2), #
    "△": (3, 2), #
    "💀": (4, 2), # x_x, xp, XP, xP, Xp, x(, x0, xo, x[, xC, xc, x{ #probably should account fo caps and lower here interchangably like the letters
    "😱": (5, 2), # :o, :O, :0, <:o, <:O, <:0, ;o, ;O, ;0, <;o, <;O, <;0
    "😁": (6, 2), # :), :], c:, C:, :}, ;), ;], c;, C;, ;}
    "😞": (7, 2), # :(, :[, :c, :C, :{, :'(, ;(, ;[, ;c, ;C, ;{, ;'(
    "😡": (8, 2), # >:(, >:[, >:c, >:C, >:{, >;(, >;[, >;c, >;C,
    "😀": (9, 2), # :D, <:D, ;D, <;D
    # maybe have that done where X is the variable that is inputted (xo, x0, (could be :, ;, or x and program autofills)
    # ROW 1
    "☀": (0, 1),
    "☁": (1, 1),
    "☂": (2, 1),
    "⛄": (3, 1),
    "🌀": (4, 1),
    "⚡": (5, 1),
    "🔨": (6, 1),
    "🎀": (7, 1),
    "✉": (8, 1),
    "$ENTER$": (9, 1), # duplicated
    # ROW 3
    "🐹": (0, 0),
    "🐱": (1, 0),
    "🐰": (2, 0),
    "🐙": (3, 0),
    "🐮": (4, 0),
    "🐷": (5, 0),
    "💰": (6, 0),
    "🐟": (7, 0),
    "🪲": (8, 0), # bug/beetle, pycharm doesnt like this one!!
    "$SPACE$": (9, 0), #duplicated
}

# if input text = uppercase, do some inputs to make that letter uppercase. maybe something to make it stay uppercase if there are more letters?
# look 1 letter ahead to determine uppercase etc

customchar = {
    "🔑": "$KEY$",
    "🗝️": "$KEY$",
    "🗝": "$KEY$",
    "--": "$LONGDASH$",
    "—": "$LONGDASH$",
    # if enter hit then "$ENTER$",
    " ": "$SPACE$",
    "•": "$DOT$", #theres more of these
    "Ææ": "$AE$",
    "×": "$MULTIPLICATION%",
    "*": "$MULTIPLICATION$",
    "«": "$LESSTHANSTACK$",
    "<<": "$LESSTHANSTACK$",
    "»": "$MORETHANSTACK",
    ">>": "$LESSTHANSTACK$",
    "‖": "$DOUBLELINEVERTICAL$",
    "ǁ": "$DOUBLELINEVERTICAL$", # apparently this is correct



}
# wonder if its better to define these in the dictionary

# for stuff that has 2 inputs (unicode and input based), make a check thats like "auto convert characters"
# like :) is the smiley face, etc

#print(customchar["🔑"])

# when going through everything make the $WORD$ accounted for (starting and stopping flag)

# all these symbols to be pasted (nook passwords online, etc) but have an emoji selection window
# maybe have all symbols be in a "symbols" thing where theyre all $LIKETHIS$ so the code interprets them better

# live typing mode (you type stuff and it queues it live, one letter after the other

# caps and shift (if caps make it go up, if shift make it go up only when held)