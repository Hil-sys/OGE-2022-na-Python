s = 0
while True:
    a=int(input())
    if a==0:
        break
    elif (a % 6 == 0) and (a % 10 == 4):
        s+=a
print(s)