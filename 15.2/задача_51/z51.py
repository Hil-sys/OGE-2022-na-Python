s = []
n = int(input())
for i in range(n):
    a = int(input())
    s.append(a)
print(min(s))
if max(s) > 80:
    print('YES')
else:
    print('NO')