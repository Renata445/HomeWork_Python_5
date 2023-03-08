def sum(a, b):
    if b == 0:
        return a
    else:
        if b > 0:
            return sum(a + 1, b - 1)
        else:
            return sum(a - 1, b + 1)

print(sum(int(input('Введите 1-ое число: ')), int(input('Введите 2-ое число: '))))