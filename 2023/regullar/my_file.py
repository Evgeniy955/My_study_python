def get_count(sentence):
    voewls = 'aeiou'
    count = 0
    for i in sentence:
        if i in voewls:
            count += 1
    return count
print(get_count("abracadabra"))
