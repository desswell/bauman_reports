class Unique(object):
    def __init__(self, items, ignore_case = False, **kwargs):
        self.set = set()
        self.items = items
        self.ignore_case = ignore_case
        self.kwargs = kwargs

    def __next__(self):
        it = iter(self.items)
        while True:
            try:
                current = next(it)
            except StopIteration:
                raise
            else:
                if self.ignore_case == True and isinstance(current, str):
                    a = current[:]
                    if a.lower() not in self.set:
                        self.set.add(a.lower())
                        return current
                elif current not in self.set:
                    self.set.add(current)
                    return current

    def __iter__(self):
        return self
if __name__ == '__main__':
    data = ["a", "A", "b", "B", "a", "A", "b", "B"]
    data1 = ["A", "a", "b"]
    print(*Unique(data))
    print(*Unique(data, True))
    print(*Unique(data1, True))