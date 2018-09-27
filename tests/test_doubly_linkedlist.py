from unittest import TestCase, main
from doubly_linkedlist import DoublyLinkedList

class UtilsTestCase(TestCase):
    def test_create_empty_DoublyLinkedList(self):
        llist = DoublyLinkedList()
        self.assertEqual('[]', str(llist))

    def test_creation_from_content(self):
        llist = DoublyLinkedList([-2, -1, 1, 3, 4, 5])
        self.assertEqual('[-2, -1, 1, 3, 4, 5]', str(llist))

    def test_append(self):
        llist = DoublyLinkedList([-2, -1, 1, 3, 4, 5])
        llist.append(7)
        self.assertEqual('[-2, -1, 1, 3, 4, 5, 7]', str(llist))

    def test_append_on_an_empty_DoublyLinkedList(self):
        llist = DoublyLinkedList()
        llist.append(7)
        self.assertEqual('[7]', str(llist))

    def test_insert_at_the_end(self):
        llist = DoublyLinkedList([-2, -1, 1, 3, 4, 5])
        llist.insert(15, 4)
        self.assertEqual('[-2, -1, 1, 3, 4, 5, 4]', str(llist))

    def test_insert_at_the_beginning(self):
        llist = DoublyLinkedList([-2, -1, 1, 3, 4, 5])
        llist.insert(0, 4)
        self.assertEqual('[4, -2, -1, 1, 3, 4, 5]', str(llist))

    def test_insert_at_the_beginning_to_empty_list(self):
        llist = DoublyLinkedList()
        llist.insert(0, 4)
        self.assertEqual('[4]', str(llist))

    def test_remove_last(self):
        llist = DoublyLinkedList([-2, -1, 1, 3, 4, 5])
        llist.remove_last()
        self.assertEqual('[-2, -1, 1, 3, 4]', str(llist))

    def test_remove_last_from_empty_list(self):
        llist = DoublyLinkedList()
        llist.remove_last()
        self.assertEqual('[]', str(llist))

    def test_reverse(self):
        llist = DoublyLinkedList([7, 14, 2, 4])
        llist.reverse()
        self.assertEqual('[4, 2, 14, 7]', str(llist))

    def test_concatenate_other(self):
        llist1 = DoublyLinkedList([2, 6, 4])
        other = DoublyLinkedList([7, 14])
        llist1.add(other)
        self.assertEqual('[2, 6, 4, 7, 14]', str(llist1))


if __name__ == '__main__':
    main()

