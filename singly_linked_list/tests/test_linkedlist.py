from unittest import TestCase

from ..main import LinkedList, Node


class LinkedListTestCase(TestCase):

    def setUp(self):
        self.llst = LinkedList()

    def test_node_class(self):
        node_a = Node(1)
        self.assertTrue(isinstance(node_a, Node))
        self.assertEqual(node_a.data, 1)
        self.assertIsNone(node_a.next)

        node_b = Node('a', node_a)
        self.assertTrue(isinstance(node_b, Node))
        self.assertEqual(node_b.data, 'a')
        self.assertEqual(node_b.next, node_a)

        node_c = Node(['a'])
        self.assertTrue(isinstance(node_c, Node))
        self.assertEqual(node_c.data, ['a'])
        self.assertIsNone(node_c.next)

    def test_linkedlist_class(self):
        self.assertTrue(isinstance(self.llst, LinkedList))
        self.assertIsNone(self.llst.head)

    def test_size(self):
        self.assertEqual(self.llst.size(), 0)
        self.llst.insert_first(1)
        self.assertEqual(self.llst.size(), 1)
        self.llst.insert_first(1)
        self.llst.insert_first(1)
        self.llst.insert_first(1)
        self.assertEqual(self.llst.size(), 4)
        self.assertEqual(len(self.llst), 4)

    def test_clear(self):
        self.llst.insert_first(1)
        self.llst.insert_first(1)
        self.llst.insert_first(1)
        self.llst.insert_first(1)
        self.assertEqual(self.llst.size(), 4)
        self.llst.clear()
        self.assertEqual(self.llst.size(), 0)

    def test_get_at(self):
        self.assertIsNone(self.llst.get_at(-10))
        self.llst.insert_last(1)
        self.assertEqual(self.llst.get_at(0).data, 1)
        self.llst.insert_last(2)
        self.llst.insert_last(3)
        self.assertEqual(self.llst.get_at(2).data, 3)
        self.assertIsNone(self.llst.get_at(7))

    def test_get_first(self):
        self.assertEqual(self.llst.get_first(), None)
        self.llst.insert_first(1)
        self.assertEqual(self.llst.get_first().data, 1)
        self.llst.insert_first(2)
        self.llst.insert_first(3)
        self.assertEqual(self.llst.get_first().data, 3)

    def test_get_last(self):
        self.assertEqual(self.llst.get_last(), None)
        self.llst.insert_first(1)
        self.assertEqual(self.llst.get_last().data, 1)
        self.llst.insert_first(2)
        self.llst.insert_first(3)
        self.assertEqual(self.llst.get_last().data, 1)

    def test_insert_at(self):
        # empty
        self.llst.insert_at(0, 'hi')
        self.assertEqual(self.llst.get_at(0).data, 'hi')
        # out of the lower bound -> prepend
        self.llst.insert_last(2)
        self.llst.insert_at(-10, 'nihao')
        self.assertEqual(self.llst.get_at(0).data, 'nihao')
        self.assertEqual(self.llst.get_at(1).data, 'hi')
        self.assertEqual(self.llst.get_at(2).data, 2)
        # in the middle
        self.llst.insert_at(1, 9)
        self.assertEqual(self.llst.get_at(0).data, 'nihao')
        self.assertEqual(self.llst.get_at(1).data, 9)
        self.assertEqual(self.llst.get_at(2).data, 'hi')
        self.assertEqual(self.llst.get_at(3).data, 2)
        # out of the upper bound -> append
        self.llst.insert_at(99, 'asdf')
        self.assertEqual(self.llst.get_at(4).data, 'asdf')
        self.assertEqual(self.llst.get_last().data, 'asdf')
        self.assertIsNone(self.llst.get_at(99))

    def test_insert_first(self):
        self.llst.insert_first(1)
        self.assertEqual(self.llst.head.data, 1)
        self.llst.insert_first(2)
        self.assertEqual(self.llst.head.data, 2)

    def test_insert_last(self):
        self.llst.insert_last(1)
        self.assertEqual(self.llst.get_last().data, 1)
        self.llst.insert_last(2)
        self.llst.insert_last(3)
        self.assertEqual(self.llst.get_last().data, 3)

    def test_remove_at(self):
        # empty
        try:
            self.llst.remove_at(4)
        except Exception as e:
            self.fail(e)
        # one
        self.llst.insert_last(1)
        self.llst.remove_at(0)
        self.assertIsNone(self.llst.get_at(0))
        # multiple
        self.llst.insert_last(2)
        self.llst.insert_last(3)
        self.llst.insert_last(4)
        self.llst.remove_at(1)
        self.assertEqual(self.llst.get_at(1).data, 4)
        # out of the lower bound -> ignore
        try:
            self.llst.remove_at(-4)
        except Exception as e:
            self.fail(e)
        self.assertEqual(self.llst.get_at(1).data, 4)
        # out of the upper bound -> ignore
        try:
            self.llst.remove_at(19)
        except Exception as e:
            self.fail(e)
        self.assertEqual(self.llst.get_at(1).data, 4)

    def test_remove_first(self):
        # empty
        try:
            self.llst.remove_first()
        except Exception as e:
            self.fail(e)
        # one element
        self.llst.insert_first(1)
        self.llst.remove_first()
        self.assertEqual(self.llst.get_first(), None)
        # multiple elements
        self.llst.insert_first(2)
        self.llst.insert_first(3)
        self.llst.insert_first(4)
        self.assertEqual(self.llst.get_first().data, 4)
        self.llst.remove_first()
        self.assertEqual(self.llst.get_first().data, 3)

    def test_remove_last(self):
        # empty
        try:
            self.llst.remove_last()
        except Exception as e:
            self.fail(e)
        # one
        self.llst.insert_first(1)
        self.llst.remove_last()
        self.assertEqual(self.llst.get_last(), None)
        # multiple
        self.llst.insert_first(2)
        self.llst.insert_first(3)
        self.llst.insert_first(4)
        self.assertEqual(self.llst.get_last().data, 2)
        self.llst.remove_last()
        self.assertEqual(self.llst.get_last().data, 3)

    def test_every(self):
        self.llst.insert_last(1)
        self.llst.insert_last(2)
        self.llst.insert_last(3)
        self.llst.insert_last(4)
        try:
            def f(node):
                node.data += 10
            self.llst.every(f)
        except Exception as e:
            self.fail(e)
        self.assertEqual(self.llst.get_at(0).data, 11)
        self.assertEqual(self.llst.get_at(1).data, 12)
        self.assertEqual(self.llst.get_at(2).data, 13)
        self.assertEqual(self.llst.get_at(3).data, 14)

    def test_iteration(self):
        ''' make it compatible with for-loops & next() function '''
        # empty
        try:
            for node in self.llst:
                node.data += 10
        except Exception as e:
            self.fail(e)
        self.assertIsNone(self.llst.get_first())
        # multiple
        self.llst.insert_last(1)
        self.llst.insert_last(2)
        self.llst.insert_last(3)
        self.llst.insert_last(4)
        # next() function
        g = iter(self.llst)
        self.assertEqual(next(g).data, 1)
        self.assertEqual(next(g).data, 2)
        self.assertEqual(next(g).data, 3)
        self.assertEqual(next(g).data, 4)
        # for-loop
        try:
            for node in self.llst:
                node.data += 10
        except Exception as e:
            self.fail(e)
        self.assertEqual(self.llst.get_at(0).data, 11)
        self.assertEqual(self.llst.get_at(1).data, 12)
        self.assertEqual(self.llst.get_at(2).data, 13)
        self.assertEqual(self.llst.get_at(3).data, 14)
