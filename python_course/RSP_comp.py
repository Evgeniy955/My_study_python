from random import choice


def game():
    while True:
        hand = input("Choose an item R - rock, S - scissors, P - paper: ").upper()
        if hand not in ["R", "S", "P"]:
            print("You entered an invalid character")
            continue
        hand_item = ["Rock", "Scissors", "Paper"]
        hand_comp = choice(hand_item)
        print(f"Сomputer element is: {hand_comp}")

        if hand_comp[0] == hand:
            print("Dead-heat")
        elif hand == "R" and hand_comp[0] == "S" or hand == "S" and hand_comp[0] == "P" \
                or hand == "P" and hand_comp[0] == "R":
            print("You won")
        else:
            print("You lost")

        game_over = input("Do you want to continue? enter Y/N: ").upper()
        if game_over not in ["Y", "N"]:
            print("Enter Y or N")

        if game_over == "Y":
            continue
        if game_over == "N":
            break


game()
