print(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'])
x = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

card_to_weight = {
    '2': 1,
    '3': 1,
    '4': 1,
    '5': 1,
    '6': 1,
    '7': 0,
    '8': 0,
    '9': 0,
    '10': -1,
    'J': -1,
    'Q': -1,
    'K': -1,
    'A': -1
}

current_hand = []

s = (input("Enter one of the characters: "))

while True:
    if s.upper() in card_to_weight.keys():
        current_hand.append(s.upper())
    elif s not in card_to_weight.keys() and s != '':
        print("Sorry, you entered an invalid character")
        break
    elif s == '':
        break
    s = input("Enter one of the characters or press enter: ")

l = 0
for k, v in card_to_weight.items():
    if k in current_hand:
        l += v

print(current_hand)
print(l)
