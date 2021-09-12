import math


def vvod_koef():
    print('Введите коэффициенты А В С: ')
    try:
        a, b, c = map(int, input().split())
        return a, b, c
    except ValueError:
        print('Не корректно введены коэффициенты')
        a, b, c = vvod_koef()
        return a, b, c


def disc(a, b, c):
    d1 = b * b - 4 * a * c
    if d1 < 0:
        noans()
        return False
    else:
        return math.sqrt(d1)


def aravnonull(b, c):
    if c * b < 0:
        x1 = math.sqrt(-c / b)
        print(f'Корни равны -{x1} {x1}', end=' ')
        return True
    else:
        return False


def korni(a, b, d):
    x1, x2 = (-b + d) / (2 * a), (-b - d) / (2 * a)
    return x1, x2


def noans():
    print("Нет решений")


a, b, c = vvod_koef()
if a != 0 and c != 0:
    d = disc(a, b, c)
    if d:
        x1, x2 = korni(a, b, d)
        if x1 < 0 and x2 > 0:
            x2 = math.sqrt(x2)
            print(f"Корнями уравнения является -{x2} {x2}")
        elif x2 < 0 and x1 > 0:
            x1 = math.sqrt(x1)
            print(f"Корнями уравнения является -{x1} {x1}")
        elif x1 > 0 and x2 > 0:
            x1, x2 = map(math.sqrt, [x1, x2])
            print(f'Корнями уравнения являются -{x1} {x1} -{x2} {x2}')
        else:
            noans()
elif c == 0:
    if not aravnonull(a, b):
        noans()
    else:
        print("и 0")
else:
    if not aravnonull(b, c):
        noans()