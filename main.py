def print_grid(grid_):
    output = "  0 1 2\n0"
    for m in range(3):
        output += " " + grid_[m]
    output += "\n1"
    for m in range(3, 6):
        output += " " + grid_[m]
    output += "\n2"
    for m in range(6, 9):
        output += " " + grid_[m]
    return print(output)


def victory(grid_, player):
    for i in range(3):
        if grid_[i] == grid_[i+3] == grid_[i+6] == player:
            return True
    for i in range(0, 7, 3):
        if grid_[i] == grid_[i + 1] == grid_[i + 2] == player:
            return True
    if grid_[0] == grid_[4] == grid_[8] == player:
        return True
    if grid_[2] == grid_[4] == grid_[6] == player:
        return True
    else:
        return False


def move(grid_, player):
    print_grid(grid_)
    print("Player", player + ", make your move!")
    invalid_move = True
    valid_values = ("0", "1", "2")
    while invalid_move:
        while True:
            i = input("Row number: ")
            if i in valid_values:
                break
            else:
                print("Invalid value")
        while True:
            j = input("Column number: ")
            if j in valid_values:
                break
            else:
                print("Invalid value")
        if grid_[int(i) * 3 + int(j)] != "-":
            print("Invalid move!")
        else:
            grid_[int(i) * 3 + int(j)] = player
            invalid_move = False
    return print_grid(grid_)


keep_playing = True
while keep_playing:
    grid = ["-" for i in range(9)]
    turn_counter = 0
    while turn_counter < 9:
        print("Move", turn_counter+1)
        if turn_counter % 2:
            move(grid, "o")
            turn_counter += 1
            if victory(grid, "o"):
                print("Naughts win!")
                break
        else:
            move(grid, "x")
            turn_counter += 1
            if victory(grid, "x"):
                print("Crosses win!")
                break
    if turn_counter - 9 and not(victory(grid, "x") or victory(grid, "o")):
        print("Draw game!")
    N = input("Enter N to stop playing, any other character to try again!").lower()
    if "n" in N:
        keep_playing = False
