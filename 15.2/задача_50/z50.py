s = []
s1 = []
while True:
    a = int(input())
    if a == 0:
        break
    s.append(a)
    if a % 2 != 0 and a % 3 == 0:
        s1.append(a)
print(len(s))
print(len(s1))