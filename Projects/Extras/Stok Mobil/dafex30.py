a_dictionary = {}
a_file = open("text.txt", 'r').read().splitlines()
for line in a_file:
    key, value, value2, value3 = line.split('#')
    a_dictionary[key] = [value, value2, value3]

def report(dictionary):
    min = None
    for k, v in dictionary.items():
        val = int(v[2])
        if (min == None):
            min = val
            max = val
            minType = k
            maxType = k
        else:
            if (min > val):
                min = val
                minType = k
            elif (max < val):
                max = val
                maxType = k
    print(f"Stok terbanyak adalah mobil dengan tipe {maxType} dengan stok {max}")
    print(f"Stok tersedikit adalah mobil dengan tipe {minType} dengan stok {min}")


def bahan_bakar(mobil):
    car = a_dictionary[mobil]
    return car[1]

print(a_dictionary)
print(bahan_bakar('avanze_S'))
report(a_dictionary)