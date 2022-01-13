s = []
n = int(input())
for i in range(n):
    a = int(input())
    if (a % 4 == 0) and (a % 7 != 0):
        s.append(a)
print(len(s))