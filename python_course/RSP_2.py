import random

should_continue = True

while should_continue:
    player_choice = input("Player choice: [R/S/P] ").lower()

    if player_choice not in ["r", "s", "p"]:
        print('Incorrect input. Try again')
        continue

    gen = {1: 'r', 2: 's', 3: 'p'}
    comp_choice = gen[random.randint(1, 3)]

    print(f'Comp choice = {comp_choice}')

    winning_combinations = [('p', 'r'), ('r', 's'), ('s', 'p')]

    if player_choice == comp_choice:
        print('A draw')
    elif (player_choice, comp_choice) in winning_combinations:
        print('Player wins')
    else:
        print('Comp wins')

    should_continue = input('Want to procced? [y/n]').lower() == 'y'
