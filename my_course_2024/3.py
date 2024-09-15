text = "Python programming is fun!"

def task_3():
    vowels = 'aeiouy'
    changed_string = ""
    count = 0
    for s in text:
        if s.lower().isalpha():
            changed_string += s
            if s in vowels:
                count += 1

    print("Number of letters in a line: ", len(changed_string))
    print("Number of vowels: ", count)
    print(text[:-1].replace(' ', '-'))

if __name__ == '__main__':
    task_3()

    # letters_count = len([char for char in text if char.isalpha()])
    # vowels = "aeiouAEIOU"
    # vowels_count = len([char for char in text if char in vowels])
    # modified_text = text.replace(" ", "-")
