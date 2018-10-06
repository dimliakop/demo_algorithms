from src.linkedlist.linkedlist import LinkedList


class Stack:
    def __init__(self, item_list=None):
        self._list = LinkedList(item_list)

    def push(self, item):
        self._list.add_first(item)

    def pop(self):
        if self._list.count == 0:
            raise ValueError("Cannot pop from an empty Stack")
        value = self._list.first.value
        self._list.remove_first()
        return value

    def peek(self):
        if self._list.count == 0:
            raise ValueError ("Cannot peek from an empty Stack")
        value = self._list.first.value
        return value

    def count(self):
        return self._list.count

    def clear(self):
        self._list.clear()

    def __str__(self):
        return str(self._list)


if __name__ == '__main__':
    main()