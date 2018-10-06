class StackArray:
    def __init__(self, _items=None):
        self._items = ()
        self._size = 0
        if not _items:
            return
        for item in _items:
            self.push(item)

    def push(self, item):
        if self._size == len(self._items):
            new_length = 4 if self._size == 0 else self._size * 2
            new_tuple = tuple((item
                               if k == len(self._items)
                               else (self._items[v]
                                     if v < len(self._items) else None)
                               for k, v in enumerate(range(new_length))))
            self._items = new_tuple
        else:
            lst = list(self._items)
            lst[self._size] = item
            self._items = tuple(lst)
        self._size += 1

    def pop(self):
        if self.count() == 0:
            raise ValueError("Cannot peek from an empty Stack")
        self._size -= 1
        return self._items[self._size]

    def peek(self):
        if self.count() == 0:
            raise ValueError("Cannot pop from an empty Stack")
        return self._items[self._size - 1]

    def count(self):
        return self._size

    def clear(self):
        self._items = ()
        self._size = 0

    def __str__(self):
        l = [self._items[i] for i in range(self._size)]
        return str(l).strip('[]')


if __name__ == '__main__':
    main()
