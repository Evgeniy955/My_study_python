alfabets = {'a': 'а', 'b': 'б', 'c': 'к', 'd': 'д', 'e': 'э', 'f': 'ф', 'g': 'г', 'h': 'х', 'i': 'і', 'j': 'дж',
            'k': 'к', 'l': 'л', 'm': 'м', 'n': 'н', 'o': 'о', 'p': 'п', 'q': 'кв', 'r': 'р', 's': 'с', 't': 'т',
            'u': 'ю', 'v': 'в', 'w': 'в', 'x': 'кс', 'y': 'ю', 'z': 'з'}


def decorator(func):
    def wrapper(*args, **kwargs):
        new_str = ''
        for i in args:
            for _ in alfabets:
                if isinstance(i, str):
                    new_str = ''.join(alfabets.get(char.lower(), char).capitalize() if char.isupper() else alfabets.get(char.lower(), char) for char in i)
            print(f"Original: {i}, Translated: {new_str}")
        return func(*args, **kwargs)
    return wrapper


@decorator
def print_string(*args):
    print('args: ', args)

if __name__ == "__main__":
    print_string("hell3o", "world", "python", "decorator", "test")
    print_string("A1bc", "xyz", "qwerty")
    print_string("A", "1", "b", "c", "d")
