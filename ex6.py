n = int(input())
c = 0

for i in range(1, n):
    c+=i*(i+1)
    if i != n-1:
        print(f"{i}*{i+1}", end='+')
    else:
        print(f"{i}*{i+1}", c, sep='=')
