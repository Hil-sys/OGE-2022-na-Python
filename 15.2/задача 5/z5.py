r = 0
k = 0
n = int(input())
s = []
for i in range(n):
    a = int(input())
    s.append(a)
    if a <= 30:
        k+=1
sm = min(s)
sx = max(s)
r = sx - sm
print(r)
print(k)
