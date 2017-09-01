
# nright angled
for i in range(9):
    print('1' * i)


# isocles-ey
for i in range(9):
    print((" " * (9 - i)) + ('1 ' * i))


def triangle(n, right=True, digit='1'):
    if right is not True:
        digit = digit + " "
    for i in range(n + 1):
        print((" " * (n - i)) + (digit * i))


def trianglegen(n, right=True, digit='1'):
    if right is not True:
        digit = digit + " "
    for i in range(n + 1):
        yield (" " * (n - i)) + (digit * i)
