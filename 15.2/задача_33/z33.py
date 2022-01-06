s = []
n = int(input())
for i in range(n):
    a = int(input())
    s.append(a)
print(max(s))
if (min(s)<20) or (max(s)>80):
    print('YES')
else:
    print('NO')