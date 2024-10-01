summ = 0
n = 0
k = 0
s = int(input())
while s != 0:
    if s % 21 == 0:
        n += 1
        summ += s
    s = int(input())
print(summ/n, n)
