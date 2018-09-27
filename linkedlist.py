

class LinkedList:
    class __Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

        def setnext(self, next):
            self.next = next

        def __repr__(self):
            return str(self.value)

    def __init__(self, node_list=None):
        self.first, self.last = None, None
        self.numItems = 0

        if node_list:
            for e in node_list:
                self.append(e)

    def append(self, item):
        node = LinkedList.__Node(item)
        if self.numItems == 0:
            self.last = node
            self.first = self.last
        else:
            cursor = self.last
            self.last = node
            cursor.next = node

        self.numItems += 1

    def insert(self, index, item):
        if index >= self.numItems:
            self.append(item)
            return

        node = LinkedList.__Node(item)
        cursor = self.first

        for i in range(1, index):
            cursor = cursor.next

        if index == 0:
            node.next = cursor
            self.first = node
        else:
            node.next = cursor.next
            cursor.next = node

        self.numItems += 1

    def remove_last(self):
        cursor = self.first
        for i in range(self.numItems):
            if cursor.next == self.last:
                cursor.next = None
                self.last = cursor
                self.numItems -= 1
            else:
                cursor = cursor.next

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

    def reverse(self):
        last = self.first
        cursor = self.first
        prev = None
        while cursor is not None:
            next = cursor.next
            cursor.next = prev
            prev = cursor
            cursor = next
        self.first = prev

    def add(self, other):
        self.last.next = other.first


if __name__ == '__main__':
    main()