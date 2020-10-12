input1 = int(input())
input2 = int(input())

def test(num):
    x1 = num // 1000
    x2 = num // 100 % 10
    x3 = num // 10 % 10
    x4 = num % 10

    if x1 == x4 and x2 == x3:
        return num
    else:
        return -1

while input1 < input2:
    x = test(input1)
    if x != -1:
        print(x)
    input1 = input1 + 1
