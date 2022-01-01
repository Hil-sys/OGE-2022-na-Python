s = []
s1 = []
n = int(input())
sr = 0
for i in range(n):
    a = int(input())
    if a > 0:
        s.append(a)
    else:
        s1.append(a)
sr = (sum(s) + sum(s1)) / (len(s) + len(s1))
print(sr)
if len(s) >= 5:
    print('YES')
else:
    print('NO')