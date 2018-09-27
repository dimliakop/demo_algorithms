from linkedlist import LinkedList

class DoublyLinkedList(LinkedList):
    class __Node:
        def __init__(self, value, next=None, previous=None):
            self.value = value
            self.next = next
            self.previous = next

        def setnext(self, next):
            self.next = next

        def setprevious(self, previous):
            self.previous = previous

        def __repr__(self):
            return str(self.value)


if __name__ == '__main__':
    main()