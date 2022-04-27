iniList = ["ayam", "goreng", "sepeda", "macaaan"]
a = "hello"
try:
    a += iniList[0][3]
except IndexError:
    a += ' '

print(a)
