filename = "secrets.txt"


def read_line():
    with open(filename, 'r') as file:
        text = [line[:1] for line in file.readlines()]

    print(''.join(text))


if __name__ == "__main__":
    read_line()
