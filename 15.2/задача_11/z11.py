s = 0
n = int(input())
for i in range(n):
    a = int(input())
    if a % 10 == 4:
        s += a
print(s)