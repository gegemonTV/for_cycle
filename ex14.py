a = int(input())
b = int(input())

for i in range(a, b+1):
    x1 = i%10
    x2 = i//10%10
    x3 = i//100%10
    x4 = i//1000

    if x1 == x2 == x3 or x1 == x2 == x4 or x1 == x3 == x4 or x2 == x3 == x4:
        print(i)
