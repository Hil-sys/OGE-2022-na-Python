k1 = 0
k2 = 0
s = []
while True:
    a = int(input())
    if a == 0:
        break
    s.append(a)
    if a > 0:
        k1 += 1
    else:
        k2 += 1
print(sum(s))
print(k1 - k2)