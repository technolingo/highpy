from unittest import TestCase

from ..main import LinkedList, Node
from ..circular import is_circular


class IsCircularTestCast(TestCase):

    def test_circular(self):
        d = Node('d')
        c = Node('c', d)
        b = Node('b', c)
        a = Node('a', b)
        d.next = b
        llst = LinkedList(a)

        self.assertEqual(llst.get_first().data, 'a')
        self.assertEqual(llst.get_first().next, b)
        self.assertEqual(is_circular(llst), True)

    def test_non_circular(self):
        d = Node('d')
        c = Node('c', d)
        b = Node('b', c)
        a = Node('a', b)
        llst = LinkedList(a)

        self.assertEqual(llst.get_first().data, 'a')
        self.assertEqual(llst.get_first().next, b)
        self.assertEqual(is_circular(llst), False)
