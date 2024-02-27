import re
import string

printable = string.printable
result = re.findall('\s', printable)
print(result)