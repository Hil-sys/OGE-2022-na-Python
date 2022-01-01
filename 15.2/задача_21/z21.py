s = []
while True:
    a = int(input())
    if a == 0:
        break
    if (a % 3 == 0) and (a % 10 == 8):
        s.append(a)
print(sum(s))