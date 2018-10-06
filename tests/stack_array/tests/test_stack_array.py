from unittest import TestCase

from src.stack_array.stack_array import StackArray


class UtilsTestCase(TestCase):
    def test_create_empty_stack(self):
        stack = StackArray()
        self.assertEqual('', str(stack))

    def test_create_stack_from_content(self):
        stack = StackArray([5, 8, 9])
        self.assertEqual('5, 8, 9', str(stack))

    def test_push_on_empty_stack(self):
        stack = StackArray()
        stack.push(6)
        self.assertEqual('6', str(stack))

    def test_push_on_non_empty_stack(self):
        stack = StackArray([4, 9])
        stack.push(6)
        self.assertEqual('4, 9, 6', str(stack))

    def test_pop_on_empty_stack(self):
        stack = StackArray()
        with self.assertRaises(ValueError):
            stack.pop()
        self.assertEqual('', str(stack))

    def test_pop_non_empty_stack(self):
        stack = StackArray([4, 9])
        value = stack.pop()
        self.assertEqual('4', str(stack))
        self.assertEqual('9', str(value))

    def test_peek_non_empty_stack(self):
        stack = StackArray([4, 9])
        value = stack.peek()
        self.assertEqual('4, 9', str(stack))
        self.assertEqual('9', str(value))

    def test_peek_empty_stack(self):
        stack = StackArray()
        with self.assertRaises(ValueError):
            stack.peek()
        self.assertEqual('', str(stack))

    def test_count_stack(self):
        stack = StackArray([4, 9])
        self.assertEqual(2, stack.count())

    def test_count_stack_empty_stack(self):
        stack = StackArray()
        self.assertEqual(0, stack.count())

    def test_clear_stack(self):
        stack = StackArray([9])
        stack.clear()
        self.assertEqual(0, stack.count())
        self.assertEqual('', str(stack))

    def test_push_pop_from_empty_to_empty_stack(self):
        stack = StackArray()
        stack.push(1)
        stack.pop()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        stack.push(5)
        stack.push(6)
        stack.push(7)
        stack.push(8)
        stack.push(9)
        self.assertEqual('1, 2, 3, 4, 5, 6, 7, 8, 9', str(stack))
        stack.pop()
        stack.push(9)
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        self.assertEqual('', str(stack))
