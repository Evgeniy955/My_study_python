import re

source = "Young Frankenstein"
search =  "n"
replace = "?"
# youpattern = re.compile(search)
# result = youpattern.match(source)
result = re.sub(search, replace, source)

print(result)
