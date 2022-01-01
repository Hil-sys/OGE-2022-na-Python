s = []
while True:
    a = int(input())
    if a == 0:
        break
    if (a % 10 == 8) and (a % 4 == 0):
        s.append(a)
print(sum(s))