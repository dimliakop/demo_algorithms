class StackArray:
    def __init__(self, item_list=None):
        self._list = list()
        if item_list:
            self._list = list(item_list)

    def push(self, item):
        self._list.insert(0, item)

    def pop(self):
        if self.count() == 0:
            raise ValueError ("Cannot peek from an empty Stack")
        return self._list.pop(0)

    def peek(self):
        if self.count() == 0:
            raise ValueError("Cannot pop from an empty Stack")
        return self._list[0]

    def count(self):
        return len(self._list)

    def clear(self):
        self._list = []

    def __str__(self):
        return str(self._list)


if __name__ == '__main__':
    main()