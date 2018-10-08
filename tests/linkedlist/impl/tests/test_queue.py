from unittest import TestCase

from src.linkedlist.impl.queue import Queue

# TODO : implement the Queue
class UtilsTestCase(TestCase):
    def test_create_empty_queue(self):
        queue = Queue()
        self.assertEqual('', str(queue))

    # def test_create_queue_from_content(self):
    #     queue = Queue(5, 8, 9)
    #     self.assertEqual('5, 8, 9', str(queue))
    #
    # def test_push_on_empty_queue(self):
    #     queue = Queue()
    #     queue.push(6)
    #     self.assertEqual('6', str(queue))
    #
    # def test_push_on_non_empty_queue(self):
    #     queue = Queue(4, 9)
    #     queue.push(6)
    #     self.assertEqual('6, 4, 9', str(queue))
    #
    # def test_pop_on_empty_queue(self):
    #     queue = Queue()
    #     with self.assertRaises(ValueError):
    #         queue.pop()
    #     self.assertEqual('', str(queue))
    #
    # def test_pop_non_empty_queue(self):
    #     queue = Queue(4, 9)
    #     value = queue.pop()
    #     self.assertEqual('9', str(queue))
    #     self.assertEqual('4', str(value))
    #
    # def test_peek_non_empty_queue(self):
    #     queue = Queue(4, 9)
    #     value = queue.peek()
    #     self.assertEqual('4, 9', str(queue))
    #     self.assertEqual('4', str(value))
    #
    # def test_peek_empty_queue(self):
    #     queue = Queue()
    #     with self.assertRaises(ValueError):
    #         queue.peek()
    #     self.assertEqual('', str(queue))
    #
    # def test_count_queue(self):
    #     queue = Queue(4, 9)
    #     self.assertEqual(2, queue.count())
    #
    def test_count_empty_queue(self):
        queue = Queue()
        self.assertEqual(0, queue.count)

    def test_clear_queue(self):
        queue = Queue()
        queue.clear()
        self.assertEqual(0, queue.count)
        self.assertEqual('', str(queue))
