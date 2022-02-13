n = int(input())
s = []
for i in range(n):
    a = int(input())
    s.append(a)
print(max(s))
if min(s) == 0:
    print('YES')
else:
    print('NO')