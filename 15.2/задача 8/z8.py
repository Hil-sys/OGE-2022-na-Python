s = []
n = int(input())
m = 0
mn = 0
for i in range(n):
    a = int(input())
    s.append(a)
m = max(s)
mn = min(s)
if mn < 30:
    c = 'YES'
else:
    c = 'NO'
print(m)
print(c)