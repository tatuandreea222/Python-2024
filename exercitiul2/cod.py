import os
stoc = input().split()
stoc = list(map(int, stoc))
print(stoc)

matrix = []
Row = (int(input("cate calculatoare tre reparate: ")))  # nr lapturi pt reparare
# Column=7 #cele 7 tipuri de piese din stoc

for row in range(Row):
    laptop = input().split()
    laptop = list(map(int, laptop))
    matrix.append(laptop)

calc_rep = 0
semnalizator = 0
# for row in range(Row):
#     a=[]
#     for column in range(7):
#         a.append(int(input()))
#     matrix.append(a)

for row in range(Row):
    semnalizator = 0
    for col in range(7):
        if matrix[row][col] == 0:
            if stoc[col] != 0:
                stoc[col] -= 1
                matrix[row][col] += 1
            else:
                for i in range(7):
                    stoc[i] += matrix[row][i]

    for i in range(7):
        if matrix[row][i] == 1:
            semnalizator += 1
    if semnalizator == 7:
        calc_rep += 1

print(calc_rep)
print(stoc)
print(matrix)
for row in range(Row):
    for column in range(7):
        print(matrix[row][column], end=" ")
    print()
os.system("PAUSE")