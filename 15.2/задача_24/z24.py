s = []
s1 = []
while True:
    a = int(input())
    if a == 0:
        break
    if a % 2 == 0:
        s1.append(a)
    else:
        s.append(a)
print(len(s) + len(s1))
print(sum(s1))