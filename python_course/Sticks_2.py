number_of_sticks = 10
player_turn = 1

def can_take(sticks):
    return sticks >= 1 and sticks<=3

def switch_player_turn(turn):
    return 1 if player_turn == 2 else 2

def end_of_game(sticks):
    return number_of_sticks <= 0

while not end_of_game(number_of_sticks):
    global taken
    print(f'How many sticks you take? Remaining {number_of_sticks}')
    try:
        taken = int(input("Take 1 to 3 sticks: "))
    except ValueError:
        print(f'You tried to take {taken}. Allowed to take 1,2,3 sticks.')
        continue

    if not can_take(taken):
        print(f'You tried to take {taken}. Allowed to take 1,2,3 sticks.')
        continue

    number_of_sticks -= taken
    print(f'Sticks taken: {taken}\n')

    if end_of_game(number_of_sticks):
        print(f'No more sticks in the game. \nPlayer {player_turn} has lost')
        break

    player_turn = switch_player_turn(player_turn)
