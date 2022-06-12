n = int(input())
s = []
for i in range(n):
    a = int(input())
    s.append(a)
print(round(sum(s)/len(s), 1))
if max(s) >= 60:
    print('YES')
else:
    print('NO')