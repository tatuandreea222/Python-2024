def factorial(j):
    d = 1
    for i in range(2, j+1):
        d *= i
    return d

k, M = input().split()
k = int(k)
M = int(M)
# print(x, y)
n = k
m = factorial(n)/factorial(n-k)
if m > M:
    n = 0
while m <= int(M):
    m = factorial(n)/factorial(n-k)
    n += 1
print(n)
