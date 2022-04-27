import re
x = 'From: Using the : character'
#greedy
y = re.findall('^F.+:', x)
print(y)
#non-greedy
y = re.findall('^F.+?:', x)
print(y)
