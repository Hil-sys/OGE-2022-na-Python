n = int(input())
m = 0
s = []
for i in range(n):
    a = int(input())
    s.append(a)
m = min(s)
if max(s) > 80:
    c = 'YES'
else:
    c = 'NO'
print(m)
print(c)