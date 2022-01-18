s = []
while True:
    a = int(input())
    if a == 0:
        break
    if (a % 8 == 0) and (a % 3 == 0):
        s.append(a)
print(len(s))
