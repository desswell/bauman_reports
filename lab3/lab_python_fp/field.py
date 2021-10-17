goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'color': 'black'}
]


def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        for it in items:
            yield it.get(args[0])
    else:
        for it in items:
            a = dict()
            for arg in args:
                if it.get(arg) != None:
                    a[arg] = it.get(arg)
            yield a

if __name__ == '__main__':
    print(*field(goods, 'title', 'price'))
    print(list(field(goods, 'title')))