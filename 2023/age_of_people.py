class GameCharacter:

    def __init__(self, name, health, level):
        self.health = health
        self.level = level
        self.name = name

    def speak(self):
        return 'Hi, my name is ' + self.name


class Villain(GameCharacter):

    def __init__(self, name, health, level):
        GameCharacter.__init__(self, name, health, level)

    def speak(self):
        return 'Hi, my name is ' + self.name + ' and I will kill you'

    def kill(self, result):
        result.health = 0
        return 'Bang-bang, now you\'re dead'


bill = GameCharacter('Bill', 50, 3)
jim = Villain('Jim', 50, 3)
print(bill.speak())
print(jim.speak())
print(jim.kill(jim))
# result = GameCharacter('Bill', 50, 3)
# print(refil.add(100))

