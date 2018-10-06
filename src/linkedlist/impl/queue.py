from src.linkedlist.linkedlist import LinkedList


class Queue:
    def __init__(self):
        self._items = LinkedList()
        self.count = 0

    def __str__(self):
        return str(self._items).strip('[]')

    def clear(self):
        self._items.clear()