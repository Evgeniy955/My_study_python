number = int(input('Enter a number: '))


def palindrome():
    tmp_original = number
    reversed_number = 0
    while tmp_original > 0:
        reversed_number = (reversed_number * 10) + tmp_original % 10
        tmp_original = tmp_original // 10

    if number == reversed_number:
        print("Palindrome")
    else:
        print("No palindrome")


palindrome()
