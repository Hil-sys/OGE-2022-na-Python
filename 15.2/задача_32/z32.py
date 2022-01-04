s = []
s1 = []
n = int(input())
for i in range(n):
    a = int(input())
    s.append(a)
    if a > 3:
        s1.append(a)
print(sum(s)/len(s))
if len(s1) >= 3:
    print('YES')
else:
    print('NO')