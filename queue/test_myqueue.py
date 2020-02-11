import unittest
from .myqueue import Queue


class QueueTestCase(unittest.TestCase):

    def test_max_length(self):
        q = Queue(max_size=2)

        q.add(1)
        self.assertEqual(len(q), 1)

        q.add(2)
        self.assertEqual(len(q), 2)

        with self.assertRaises(Exception):
            q.add(3)

        self.assertEqual(q.get(), 1)
        self.assertEqual(len(q), 1)

        self.assertEqual(q.get(), 2)
        self.assertEqual(len(q), 0)

        with self.assertRaises(Exception):
            q.get()


if __name__ == "__main__":
    unittest.main()
