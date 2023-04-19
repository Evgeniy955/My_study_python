def sticks():
    number_of_sticks = 10
    player_turn = 1

    while number_of_sticks > 0:
        print(f'How many sticks you take? Remaining {number_of_sticks}')
        try:
            taken = int(input("Take 1 to 3 sticks: "))
        except ValueError:
            print("You didn't enter an integer. Try again")
            continue

        if taken < 1 or taken > 3:
            print(f'You tried to take {taken}. Allowed to take 1,2,3 sticks.')
            continue

        number_of_sticks -= taken
        print(f'Sticks taken: {taken}\n')

        if number_of_sticks <=0:
            print(f'No more sticks in the game. \n Player {player_turn} has lost')

        player_turn = 1 if player_turn == 2 else 2


sticks()