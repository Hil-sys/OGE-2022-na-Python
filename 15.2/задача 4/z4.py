s = 0
for i in range(5):
    a = int(input())
    if (a % 4 == 0) and (a % 10 == 6):
        s += a
print(s)