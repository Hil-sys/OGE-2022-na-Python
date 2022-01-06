s = []
n = int(input())
for i in range(n):
    a = int(input())
    if a % 10 == 2:
        s.append(a)
print(len(s))
print(max(s))