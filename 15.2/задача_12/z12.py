s = []
n = int(input())
for i in range(n):
    a = int(input())
    if a % 5 == 0:
        s.append(a)
print(sum(s))