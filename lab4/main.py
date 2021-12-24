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
def get_roots(a, b, c):
    result = []
    if a != 0 and c != 0:
        d = disc(a, b, c)
        if d:
            x1, x2 = korni(a, b, d)
            if x1 < 0 and x2 > 0:
                x2 = math.sqrt(x2)
                # print(f"Корнями уравнения является -{x2} {x2}")
                result.append(-x2)
                result.append(x2)
            elif x2 < 0 and x1 > 0:
                x1 = math.sqrt(x1)
                result.append(-x1)
                result.append(x1)
                # print(f"Корнями уравнения является -{x1} {x1}")
            elif x1 > 0 and x2 > 0:
                x1, x2 = map(math.sqrt, [x1, x2])
                result.append(x1)
                result.append(-x1)
                result.append(x2)
                result.append(-x2)
                # print(f'Корнями уравнения являются -{x1} {x1} -{x2} {x2}')
            else:
                noans()
        elif d == 0:
            if b > 0:
                noans()
            else:
                x1 = math.sqrt(-b / 2 * a)
                # print(f'Корниями уравнения являются -{x1} {x1}')
                result.append(-x1)
                result.append(x1)
    # elif a == 0 and b == 0 and c == 0:
    #     print("Решением являются все действительные числа")
    elif a == 0 and c == 0:
        print('Решением является 0')
        result.append(0)
    elif c == 0:
        if not aravnonull(a, b):
            pass
        #noans()
        else:
            result.append(0)
    # else:
    #     if not aravnonull(b, c):
    #         noans()
    return result
if __name__ == "__main__":
    a, b, c = vvod_koef()
    print(get_roots(a, b, c))