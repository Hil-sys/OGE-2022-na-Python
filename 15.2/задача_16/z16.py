s = []
n = int(input())
for i in range(n):
    a = int(input())
    if a % 10 == 3:
        s.append(a)
print(max(s))