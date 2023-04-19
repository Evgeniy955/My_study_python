bones = [(1, 2), (3, 4), (5, 6)]

def  calc_dice_scores(list):
    calc = 0
    for i in bones:
        if i[0] == i[1]:
            return 0
        else:
            calc += sum(i)
    return calc
print(calc_dice_scores(bones))

# return sum([a+b for a,b in bones]) if not any([a==b for a, b in bones]) else 0
