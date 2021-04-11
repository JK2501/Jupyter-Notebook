src = 'Data2.txt'
i = 0

with open(src, 'r') as r:
    lines = r.readlines()
    for line in lines:
        i += 1
        print(i)

print(i)
