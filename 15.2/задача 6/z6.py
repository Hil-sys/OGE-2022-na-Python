s = []
m = 0
n = int(input())
for i in range(n):
    a = int(input())
    s.append(a)
m = min(s)
if m < -15:
    c = 'YES'
else:
    c = 'NO'
print(m)
print(c)