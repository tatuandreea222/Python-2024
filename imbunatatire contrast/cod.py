import math
linii = int(input())
col = int(input())

originala = []
for linie in range(linii):
    a = []
    for coll in range(col):
        a.append(int(input()))
    originala.append(a)

filtrata = []
for linie in range(linii):
    a = []
    for coll in range(col):
        f, i = math.modf(originala[linie][coll]*0.9 + 2)
        a.append(round(i))
    filtrata.append(a)


# diferenta = []
# for linie in range(linii):
#     for coll in range(col):
#         diferenta.append(filtrata[linie][coll] - originala[linie][coll])
#
# print(diferenta)
medie = 0
for linie in range(linii):
    for coll in range(col):
        medie += (filtrata[linie][coll] - originala[linie][coll])

medie /= (linii*col)
print(round(medie, 2))