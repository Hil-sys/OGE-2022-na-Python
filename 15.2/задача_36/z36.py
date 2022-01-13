s = []
s1 = []
n = int(input())
for i in range(n):
    a = int(input())
    if a < 5:
        s.append(a)
    if a == 10:
        s1.append(a)
print(len(s))
if len(s1) > 0:
    print('YES')
else:
    print('NO')