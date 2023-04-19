import re

source = '''I wish I may, I wish I might
        Have a dish of fish tonight.'''
result = re.findall('I (?=wish)', source)

print(result)