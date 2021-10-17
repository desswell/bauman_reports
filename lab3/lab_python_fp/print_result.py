def print_result(func):
    def decorated_func(*args, **kwargs):
        fun = func(*args, **kwargs)
        print(func.__name__)
        if isinstance(fun, list):
            if isinstance(fun[0], tuple):
                for i in fun:
                    print(*i, end=' ')
            else:
                print(*fun)
        elif isinstance(fun, dict):
            for a, b in fun.items():
                print(f'{a} = {b}')
        else:
            print(fun)
        return fun
    return decorated_func

@print_result
def test_1():
    return 1

@print_result
def test_2():
    return 'iu5'

@print_result
def test_3():
    return {'a': 1, 'b': 2}

@print_result
def test_4():
    return [1, 2]

if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
    test_4()