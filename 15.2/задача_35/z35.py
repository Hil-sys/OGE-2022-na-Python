s = []
while True:
    a = int(input())
    if a == 0:
        break
    if (a > 9) and (a < 100) and (a % 8 == 0):
        s.append(a)
print(sum(s))