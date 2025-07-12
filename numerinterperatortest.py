path_y = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 4]


for lister_func in path_y:
    if lister_func == 1:
        print("move up")
    elif lister_func == 2:
        print("move down")
    elif lister_func == 3:
        print("move left")
    elif lister_func == 4:
        print("move right")
    else:
        print("????? INVALID NUMBER ?????")

#cursor_move = 4
#if cursor_move == 1:
#    print("move up")
#elif cursor_move == 2:
#    print("move down")
#elif cursor_move == 3:
#    print("move left")
#elif cursor_move == 4:
#    print("move right")
#else:
#    print("I don't know where to go.")