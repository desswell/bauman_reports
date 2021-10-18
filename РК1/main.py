from operator import itemgetter

class hd:
    """Жесткий диск"""

    def __init__(self, id, mf, cost, comp_id):
        self.id = id
        self.mf = mf
        self.cost = cost
        self.comp_id = comp_id


class comp:
    """Компьютер"""

    def __init__(self, id, OS):
        self.id = id
        self.OS = OS

class hdcomp:
    """
    'Жесткие диски компютеров' для реализации
    связи многие-ко-многим
    """

    def __init__(self, disk_id, comp_id):
        self.disk_id = disk_id
        self.comp_id = comp_id

comps = [
    comp(1, 'Lunix'),
    comp(2, 'Windows'),
    comp(3, 'Lunix'),
    comp(123, 'Mac OS'),
    comp(321, 'Mac OS'),
    comp(3223123, 'Windows')
]

hds = [
    hd(321, 'Seagate', 3500, 1),
    hd(123, 'WD', 2500, 2),
    hd(13, 'Toshiba', 4500, 3),
    hd(14, 'WD', 2500, 3),
    hd(154, 'Apple', 10000, 123),
]
hdcomps = [
    hdcomp(321, 1),
    hdcomp(123, 2),
    hdcomp(13, 3),
    hdcomp(14, 3),
    hdcomp(154, 123),
]

"""Основная функция"""

# Соединение данных один-ко-многим
one_to_many = [(e.mf, e.cost, d.OS)
               for d in comps
               for e in hds
               if e.comp_id == d.id]

# Соединение данных многие-ко-многим
many_to_many_temp = [(d.OS, ed.comp_id, ed.disk_id)
                     for d in comps
                     for ed in hdcomps
                     if d.id == ed.comp_id]

many_to_many = [(e.mf, e.cost, OS)
                for OS, comp_id, disk_id in many_to_many_temp
                for e in hds if e.id == disk_id]

print('Задание Б1')
res_11 = sorted(one_to_many, key=itemgetter(2))
print(res_11)

print('\nЗадание Б2')
a = list(set([i.OS for i in comps]))
res_12 = sorted([(i, len([j for j in many_to_many_temp if i == j[0]])) for i in a], key=itemgetter(1))
print(res_12)

print('\nЗадание Б3')
b = [j for j in many_to_many if j[0][-1:] == 'e']
res_13 = {j[2]: [i[0] for i in b if i[2] == j[2]] for j in b}
print(res_13)