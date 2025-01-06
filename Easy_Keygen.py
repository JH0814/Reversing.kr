serial = 0x5B134977135E7D13
key = 0x1020301020301020
res = serial ^ key
res = hex(res)
for i in range(2, len(res), 2):
    print(chr(int("0x" + res[i:i+2], 16)), end='')
print()