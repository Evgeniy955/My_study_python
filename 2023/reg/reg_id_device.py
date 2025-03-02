import re

source = "    iPad Pro (12.9-inch) (6th generation) (F21603F1-00B7-4962-881D-2B18E3A295FB) (Booted) \n"
index_start = source.count("i")+1
name_line = ' '.join(source.split(" ")[:-3]) + ' '
udid = source.split(" ")[-3].replace("(", "").replace(")", "")

name = name_line[index_start:]

print(name)
print(udid)

