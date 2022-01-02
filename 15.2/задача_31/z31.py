s = []
n = int(input())
for i in range(n):
    a = int(input())
    if a % 10 == 4:
        s.append(a)
print(min(s))