n = int(input())
b = 0
for i in range(n):
    a = int(input())
    if a % 6 == 0:
        b += a
print(b)
