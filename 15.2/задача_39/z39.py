n = int(input())
s = []
s1 = []
for I in range(n):
    a = int(input())
    if a == 5:
        s.append(a)
    if a <= 2:
        s1.append(a)
print(len(s))
if len(s1) >= 2:
    print('YES')
else:
    print('NO')
