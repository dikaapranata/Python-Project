# d = {'a' : 10, 'c' : 1, 'b' : 22}
# # print(d.items())
# # print(sorted(d.items()))
# # print(d)
# for k, v in sorted(d.items()):
#     print(k, v)

# c = {'a': 10, 'd' : 21, 'z' : 3}
# tmp = list()
# for k, v in c.items():
#     tmp.append((v,k))
# print(tmp)
# tmp = sorted(tmp, reverse=True)
# print(tmp)

fhand = open('text.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()
for k, v in counts.items():
    newtup = (v, k)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

for v, k in lst[:5]:
    print(k, v)