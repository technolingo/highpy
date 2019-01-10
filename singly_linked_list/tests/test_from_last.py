from unittest import TestCase

from ..main import LinkedList
from ..from_last import get_nth_node_from_last


class FromLastTestCast(TestCase):

    def setUp(self):
        self.llst = LinkedList()

    def test_empty(self):
        self.assertIsNone(get_nth_node_from_last(self.llst, 5))

    def test_zeroth(self):
        self.llst.insert_last('a')
        self.llst.insert_last('b')
        self.assertEqual(get_nth_node_from_last(self.llst, 0).data, 'a')

    def test_normal(self):
        self.llst.insert_last('a')
        self.llst.insert_last('b')
        self.llst.insert_last('c')
        self.llst.insert_last('d')
        self.llst.insert_last('e')
        self.llst.insert_last('f')
        self.llst.insert_last('g')
        self.assertEqual(get_nth_node_from_last(self.llst, 2).data, 'e')
        self.assertEqual(get_nth_node_from_last(self.llst, 4).data, 'c')
        self.assertEqual(get_nth_node_from_last(self.llst, 5).data, 'b')
