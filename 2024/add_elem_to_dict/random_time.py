from random import randint

def new_data():
    any_int = randint(100, 501)
    new_str = f"run_{randint(1,10)}: {any_int} seconds"
    return new_str

new_data()