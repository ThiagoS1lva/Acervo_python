m = []
aux = 0
mt = []

for i in range (0, 3):
    m.append([])
    mt.append([])
    for j in range (0,3):
        m[i].append(int(input("element:")))
        mt[i].append(0)

for x in range (0, 3):
    for y in range (0, 3):
        mt[x][y] = m[y][x]

print(m)
print(mt)
