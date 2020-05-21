game = [["","",""],
        ["","",""],
        ["","",""]]


def game_state():
    for line in game:
        print (line)


def win_condition():
    global game
    #checking horizontal lines
    if game[0][0] == game[0][1] == game[0][2] and game[0][0] != "":
        print("Game won by", game[0][0])
        quit()
    if game[1][0] == game[1][1] == game[1][2] and game[1][0] != "":
        print("Game won by", game[1][0])
        quit()
    if game[2][0] == game[2][1] == game[2][2] and game[2][0] != "":
        print("Game won by", game[2][0])
        quit()
    # checking vertical lines
    if game[0][0] == game[1][0] == game[2][0] and game[0][0] != "":
        print("Game won by", game[0][0])
        quit()
    if game[0][1] == game[1][1] == game[2][1] and game[0][1] != "":
        print("Game won by", game[0][1])
        quit()
    if game[0][2] == game[1][2] == game[2][2] and game[0][2] != "":
        print("Game won by", game[0][2])
        quit()
    #checking diagonal lines
    if game[0][0] == game[1][1] == game[2][2] and game[0][0] != "":
        print("Game won by", game[0][0])
        quit()
    if game[0][2] == game[1][1] == game[2][0] and game[0][2] != "":
        print("Game won by", game[0][2])
        quit()


def put_x():
    print("X turn")
    game_state()
    x = int(input("Type row (1-3): ")) - 1
    y = int(input("Type column (1-3): ")) - 1
    global game
    if x < 4 and y < 4:
        if game[x][y] == "":
            game[x][y] = "X"
        else:
            print("Square is not empty")
            put_x()
        win_condition()
    else:
        print("Type row and column smaller than 4")
        put_x()
    put_o()


def put_o():
    print("O turn")
    game_state()
    x = int(input("Type row (1-3): ")) - 1
    y = int(input("Type column (1-3): ")) - 1
    global game
    if x < 4 and y < 4:
        if game[x][y] == "":
            game[x][y] = "O"
        else:
            print("Square is not empty")
            put_o()
        win_condition()
    else:
        print("Type row and column smaller than 4")
        put_o()
    put_x()


choice = input("Do you want to play a game of tic tac toe (Y/N): ")
if choice == "Y" or choice == "y":
    x_or_o = input("Who begins (X/O): ")
    if x_or_o == "X" or x_or_o == "x":
        put_x()
    elif x_or_o == "O" or x_or_o == "o":
        put_o()
    else:
        print("Choose X/0")

elif choice == "N" or choice == "n":
    print("Thx for playing")
else:
    print("Choose Y/N")
