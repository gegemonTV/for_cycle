n = int(input())
c = 0
x = 1
for i in range(1, n+1):
    x *= i
    c+=x
print(c)
