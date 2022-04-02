s = []
while True:
    a = int(input())
    if a == 0:
        break
    s.append(a)
s.sort()
print(s[0]+s[1])
print(s[-1]+s[-2])
