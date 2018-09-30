

class DoublyLinkedList:
    class __Node:
        def __init__(self, value, next=None, previous=None):
            self.value = value
            self.next = next
            self.next = previous

        def __repr__(self):
            return str(self.value)

    def __init__(self, node_list=None):
        self.first, self.last = None, None
        self.count = 0

        if node_list:
            for e in node_list:
                self.append(e)

    def append(self, item):
        node = DoublyLinkedList.__Node(item)
        if self.count == 0:
            self.last = node
            self.first = self.last
            self.first.previous = None
        else:
            cursor = self.last
            node.previous = cursor
            self.last = node
            cursor.next = node

        self.count += 1

    def insert(self, index, item):
        if index >= self.count:
            self.append(item)
            return

        node = DoublyLinkedList.__Node(item)
        cursor = self.first

        for i in range(1, index):
            cursor = cursor.next

        if index == 0:
            cursor.previous = node
            node.next = cursor
            self.first = node
        else:
            node.next = cursor
            node.previous = cursor.previous
            cursor.previous = node

        self.count += 1

    def remove_first(self):
        if self.count == 0:
            return
        self.first = self.first.next
        self.first.previous = None
        self.count -= 1
        if self.count == 0:
            self.last = None

    def remove_last(self):
        if self.count == 0:
            return
        self.last.previous.next = None
        self.last = self.last.previous
        self.count -= 1

    def __str__(self):
        ret = []
        if self.first == None:
            return str(ret)
        cursor = self.first
        ls = [cursor]
        while cursor.next is not None:
            cursor = cursor.next
            ls.append(cursor)
        return str(ls)

    def clear(self):
        self.first = None
        self.last = self.first
        self.count = 0

    def add(self, other):
        if other.count == 0:
            return
        if self.count == 0:
            self.first = other.first
        else:
            self.last.next = other.first

    def reverse(self):
        if self.count == 0:
            return
        dl = DoublyLinkedList()
        cursor = self.last
        dl.append(cursor)
        while cursor is not None:
            dl.append(cursor.previous)
            cursor = cursor.previous
            if cursor.previous is None:
                break

        self.clear()
        self.add(dl)


if __name__ == '__main__':
    main()