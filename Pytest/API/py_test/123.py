import math

x = [
    "5.3*96",
    "180-65.68412",
    "2.126+95.321354656",
    "122/11",
    "Error: Property name expected after dot (char 13)"
]
round_res = 3

l = ['%.{}g'.format(round_res) % (5.3*96), '%.{}g'.format(round_res) % (180-65.68412),
     '%.{}g'.format(round_res) % (2.126+95.321354656), '%.{}g'.format(round_res) % (122/11),
     "Error: Property name expected after dot (char 13)"]
# res = ['%.{}g'.format(round_res) % i for i in l]
# res = ['%.{}g'.format(round_res) % i for i in x]
print(l)
# print(res)




z = math.sqrt(11111111)
# c = list(reversed(z.split()))[0]
# x = eval(c)
# print('%.5g' % x)
x = '%.{}g'.format(round_res) % z
p = str(x)
# print(float(x))
# print(eval(c))

# l = [eval(list(i.split())[-1]) for i in x]
# # res = ['%.{}g'.format(round_res) % i for i in l]
# res = ['%.{}g'.format(round_res) % i for i in l]