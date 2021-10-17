import json

from lab_python_fp import print_result, field, gen_random, unique, cm_timer

path = 'data_light.json'
try:
    with open(path) as f:
        data = json.load(f)
except FileNotFoundError:
    print('Неверно указан путь к файлу')
    raise SystemExit

@print_result.print_result
def f1(arg):
    return sorted(unique.Unique(list(field.field(arg, 'job-name'))))


@print_result.print_result
def f2(arg):
    return list(filter(lambda x: True if 'программист' in x else False, arg))


@print_result.print_result
def f3(arg):
    return list(map(lambda x: x + ' с опытом Python', arg))


@print_result.print_result
def f4(arg):
    a = list(gen_random.gen_random(len(arg), 100000, 200000))
    a = ['зарплата ' + str(i) + ' руб.' for i in a]
    return list(zip(arg, a))


if __name__ == '__main__':
    with cm_timer.cm_timer_1():
        f4(f3(f2(f1(data))))
