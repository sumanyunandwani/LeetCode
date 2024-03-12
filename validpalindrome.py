import re
str = "0P"

pattern = re.compile('[a-z]')
check_string = pattern.findall(str.lower())
print(check_string)
if check_string == check_string[::-1]:
    print(True)
print(False)
