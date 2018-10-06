from unittest import TestCase

from src.linkedlist.impl.stack import Stack


class UtilsTestCase(TestCase):
    def test_create_empty_stack(self):
        stack = Stack()
        self.assertEqual('[]', str(stack))

    def test_create_stack_from_content(self):
        stack = Stack([5, 8, 9])
        self.assertEqual('[5, 8, 9]', str(stack))

    def test_push_on_empty_stack(self):
        stack = Stack()
        stack.push(6)
        self.assertEqual('[6]', str(stack))

    def test_push_on_non_empty_stack(self):
        stack = Stack([4, 9])
        stack.push(6)
        self.assertEqual('[6, 4, 9]', str(stack))

    def test_pop_on_empty_stack(self):
        stack = Stack()
        with self.assertRaises(ValueError):
            stack.pop()
        self.assertEqual('[]', str(stack))

    def test_pop_non_empty_stack(self):
        stack = Stack([4, 9])
        value = stack.pop()
        self.assertEqual('[9]', str(stack))
        self.assertEqual('4', str(value))

    def test_peek_non_empty_stack(self):
        stack = Stack([4, 9])
        value = stack.peek()
        self.assertEqual('[4, 9]', str(stack))
        self.assertEqual('4', str(value))

    def test_peek_empty_stack(self):
        stack = Stack()
        with self.assertRaises(ValueError):
            stack.peek()
        self.assertEqual('[]', str(stack))

    def test_count_stack(self):
        stack = Stack([4, 9])
        self.assertEqual(2, stack.count())

    def test_count_stack_empty_stack(self):
        stack = Stack()
        self.assertEqual(0, stack.count())

    def test_clear_stack(self):
        stack = Stack([9])
        stack.clear()
        self.assertEqual(0, stack.count())
        self.assertEqual('[]', str(stack))