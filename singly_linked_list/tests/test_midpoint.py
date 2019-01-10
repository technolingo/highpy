from unittest import TestCase

from ..main import LinkedList
from ..midpoint import midpoint


class MidpointTestCase(TestCase):

    def setUp(self):
        self.llst = LinkedList()

    def test_empty(self):
        self.assertIsNone(midpoint(self.llst))

    def test_odd(self):
        self.llst.insert_last('a')
        self.assertEqual(len(self.llst), 1)
        self.assertEqual(midpoint(self.llst).data, 'a')
        self.llst.insert_last('b')
        self.llst.insert_last('c')
        self.assertEqual(len(self.llst), 3)
        self.assertEqual(midpoint(self.llst).data, 'b')
        self.llst.insert_last('d')
        self.llst.insert_last('e')
        self.assertEqual(len(self.llst), 5)
        self.assertEqual(midpoint(self.llst).data, 'c')
        self.llst.insert_last('f')
        self.llst.insert_last('g')
        self.llst.insert_last('h')
        self.llst.insert_last('i')
        self.assertEqual(len(self.llst), 9)
        self.assertEqual(midpoint(self.llst).data, 'e')

    def test_even(self):
        self.llst.insert_last('a')
        self.llst.insert_last('b')
        self.assertEqual(len(self.llst), 2)
        self.assertEqual(midpoint(self.llst).data, 'a')
        self.llst.insert_last('c')
        self.llst.insert_last('d')
        self.assertEqual(len(self.llst), 4)
        self.assertEqual(midpoint(self.llst).data, 'b')
        self.llst.insert_last('e')
        self.llst.insert_last('f')
        self.llst.insert_last('g')
        self.llst.insert_last('h')
        self.assertEqual(len(self.llst), 8)
        self.assertEqual(midpoint(self.llst).data, 'd')
