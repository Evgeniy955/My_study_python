from monostate import Monostate
from module_two import two

def one():
    return Monostate().data * 100

if __name__ == '__main__':
    result = one() + two()
    print(result)
