text = "Python programming is fun!"

def task_3():
    vowels = 'aeiouy'
    changed_string = ""
    count = 0
    for s in text:
        if s.lower().isalnum():
            changed_string += s
        for letter in vowels:
            if s == letter:
                count += 1

    print("Number of letters in a line: ", len(changed_string))
    print("Number of vowels: ", count)
    print(text[:-1].replace(' ', '-'))

if __name__ == '__main__':
    task_3()