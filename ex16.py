n = int(input())
c = 0
for i in range(1, n+1):
    for _ in range(i):
        print(i , end = " ")
        c +=1
        if c>i:
            break
    if c>i:
        break
