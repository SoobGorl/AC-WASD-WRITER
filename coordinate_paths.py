letters_qwerty = {
    # ROW 0
    "!": (0,0),
    "?": (1,0),
    "\"": (2,0),
    "-": (3,0),
    "~": (4,0),
    "$LONGDASH$": (5,0),
    "\'": (6,0),
    ";": (7,0),
    ":": (8,0),
    "$KEY$": (9,0),
    # ROW 1
    "q": (0,1),
    "w": (1,1),
    "e": (2,1),
    "r": (3,1),
    "t": (4,1),
    "y": (5,1),
    "u": (6,1),
    "i": (7,1),
    "o": (8,1),
    "p": (9,1),
    # ROW 2
    "a": (0, 2),
    "s": (1, 2),
    "d": (2, 2),
    "f": (3, 2),
    "g": (4, 2),
    "h": (5, 2),
    "j": (6, 2),
    "k": (7, 2),
    "l": (8, 2),
    "$ENTER$": (9, 2),
    # ROW 3
    "z": (0, 3),
    "x": (1, 3),
    "c": (2, 3),
    "v": (3, 3),
    "b": (4, 3),
    "n": (5, 3),
    "m": (6, 3),
    ",": (7, 3),
    ".": (8, 3),
    "$SPACE$": (9, 3),
}

letters_upper = {
    # ROW 0
    "1": (0,0),
    "2": (1,0),
    "3": (2,0),
    "4": (3,0),
    "5": (4,0),
    "6": (5,0),
    "7": (6,0),
    "8": (7,0),
    "9": (8,0),
    "0": (9,0),
}

# figure out how to differenciate between these, do I just copy the other rows into here? might be good for sanity sake
letters_asdf = {
    # ROW 0
    "$DOT$": (9,0),
    # ROW 1
    "a": (0, 1),
    "b": (1, 1),
    "c": (2, 1),
    "d": (3, 1),
    "e": (4, 1),
    "f": (5, 1),
    "g": (6, 1),
    "h": (7, 1),
    "i": (8, 1),
    "j": (9, 1),
    # ROW 2
    "k": (0, 2),
    "l": (1, 2),
    "m": (2, 2),
    "n": (3, 2),
    "o": (4, 2),
    "p": (5, 2),
    "q": (6, 2),
    "r": (7, 2),
    "s": (8, 2),
    "$ENTER$": (9, 2), # duplicated
    # ROW 3
    "t": (0, 3),
    "u": (1, 3),
    "v": (2, 3),
    "w": (3, 3),
    "x": (4, 3),
    "y": (5, 3),
    "z": (6, 3),
    ",": (7, 3), # duplicated
    ".": (8, 3), # duplicated
    "$SPACE$": (9, 3) # duplicated
}

punct = {
    # ROW 0
    "#": (0,0),
    "?": (1,0), # duplicated
    "\"": (2,0), # duplicated
    "-": (3,0), # duplicated
    "$": (4,0), # duplicated
    "$LONGDASH$": (5,0), # duplicated
    "7": (6,0), # duplicated
    "8": (7,0), # duplicated
    "9": (8,0), # duplicated
    "$AE$": (9,0),
    # ROW 1
    "%": (0, 1),
    "&": (1, 1),
    "@": (2, 1),
    "_": (3, 1),
    "‾": (4, 1),
    "/": (5, 1),
    "¦": (6, 1), # its like a thick colon
    "$MULTIPLICATION$": (7, 1),
    "÷": (8, 1),
    "=": (9, 1),
    # ROW 2
    "(": (0, 2),
    ")": (1, 2),
    "<": (2, 2),
    ">": (3, 2),
    "$LESSTHANSTACK$": (4, 2),
    "$MORETHANSTACK$": (5, 2),
    "⚞": (6, 2),
    "⚟": (7, 2),
    "+": (8, 2),
    "$ENTER$": (9, 2),  # duplicated
    # ROW 3
    "β": (0, 3),
    "þ": (1, 3),
    "ð": (2, 3),
    "§": (3, 3),
    "$DOUBLELINEVERTICAL$": (4, 3),
    "μ": (5, 3),
    "¬": (6, 3),
    ",": (7, 3),  # duplicated
    ".": (8, 3),  # duplicated
    "$SPACE$": (9, 3)  # duplicated
}

# credits to https://sheet.shiar.nl/keyboard/altgr/animal, helped with tracking down unicode for these + punct
icons = {
    # ROW 0
    "♥": (0,0), # MANY HEARTS, ACCOUNT FOR ALL OF THEM!!! SAME GOES FOR A LOT OF THESE ICONS!
    "★": (1,0),
    "♪": (2,0),
    "💧": (3,0),
    "💢": (4,0),
    "❀": (5,0), #
    "🐾": (6,0),
    "♂": (7,0),
    "♀": (8,0),
    "∞": (9,0),
    # ROW 1
    "○": (0,1), #
    "☓": (1,1),
    "□": (2,1), #
    "△": (3,1), #
    "💀": (4,1), # x_x, xp, XP, xP, Xp, x(, x0, xo, x[, xC, xc, x{ #probably should account fo caps and lower here interchangably like the letters
    "😱": (5,1), # :o, :O, :0, <:o, <:O, <:0, ;o, ;O, ;0, <;o, <;O, <;0
    "😁": (6,1), # :), :], c:, C:, :}, ;), ;], c;, C;, ;}
    "😞": (7,1), # :(, :[, :c, :C, :{, :'(, ;(, ;[, ;c, ;C, ;{, ;'(
    "😡": (8,1), # >:(, >:[, >:c, >:C, >:{, >;(, >;[, >;c, >;C,
    "😀": (9,1), # :D, <:D, ;D, <;D
    # maybe have that done where X is the variable that is inputted (xo, x0, (could be :, ;, or x and program autofills)
    # ROW 2
    "☀": (0, 2),
    "☁": (1, 2),
    "☂": (2, 2),
    "⛄": (3, 2),
    "🌀": (4, 2),
    "⚡": (5, 2),
    "🔨": (6, 2),
    "🎀": (7, 2),
    "✉": (8, 2),
    "$ENTER$": (9, 2), # duplicated
    # ROW 3
    "🐹": (0, 3),
    "🐱": (1, 3),
    "🐰": (2, 3),
    "🐙": (3, 3),
    "🐮": (4, 3),
    "🐷": (5, 3),
    "💰": (6, 3),
    "🐟": (7, 3),
    "🪲": (8, 3), # bug/beetle, pycharm doesnt like this one!!
    "$SPACE$": (9, 3), #duplicated
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

print(customchar["🔑"])

# when going through everything make the $WORD$ accounted for (starting and stopping flag)

# all these symbols to be pasted (nook passwords online, etc) but have an emoji selection window
# maybe have all symbols be in a "symbols" thing where theyre all $LIKETHIS$ so the code interprets them better

# live typing mode (you type stuff and it queues it live, one letter after the other