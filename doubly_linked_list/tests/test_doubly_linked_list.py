import pytest

from ..main import DoublyLinkedList, Node


class TestDoublyLinkedList:
    def setup_method(self):
        self.dllst = DoublyLinkedList()

    def test_node_class(self):
        node_a = Node(1)
        assert isinstance(node_a, Node)
        node_b = Node('a', None, node_a)
        assert isinstance(node_b, Node)
        node_c = Node(['c'], node_a, node_b)
        assert isinstance(node_c, Node)
        assert node_c.prev.data == node_a.data
        assert node_c.next == node_b

    def test_doubly_linked_list_class(self):
        assert isinstance(self.dllst, DoublyLinkedList)
        assert self.dllst.head is None
        assert self.dllst.tail is None

    def test_size(self):
        assert self.dllst.size() == 0
        self.dllst.insert_first(1)
        assert self.dllst.size() == 1
        self.dllst.insert_first(1)
        self.dllst.insert_first(1)
        self.dllst.insert_first(1)
        assert self.dllst.size() == 4
        assert len(self.dllst) == 4

    def test_clear(self):
        self.dllst.insert_first(1)
        self.dllst.insert_first(1)
        self.dllst.insert_first(1)
        self.dllst.insert_first(1)
        assert self.dllst.size() == 4
        self.dllst.clear()
        assert self.dllst.size() == 0

    def test_get_at(self):
        assert self.dllst.get_at(-10) is None
        self.dllst.insert_last(1)
        assert self.dllst.get_at(0).data == 1
        self.dllst.insert_last(2)
        self.dllst.insert_last(3)
        assert self.dllst.get_at(2).data == 3
        assert self.dllst.get_at(7) is None

    def test_get_first(self):
        assert self.dllst.get_first() is None
        self.dllst.insert_first(1)
        assert self.dllst.get_first().data == 1
        self.dllst.insert_first(2)
        self.dllst.insert_first(3)
        assert self.dllst.get_first().data == 3

    def test_get_last(self):
        assert self.dllst.get_last() is None
        self.dllst.insert_first(1)
        assert self.dllst.get_last().data == 1
        self.dllst.insert_first(2)
        self.dllst.insert_first(3)
        assert self.dllst.get_last().data == 1

    def test_insert_at(self):
        # empty
        self.dllst.insert_at(0, 'hi')
        assert self.dllst.get_at(0).data == 'hi'
        # out of the lower bound
        with pytest.raises(ValueError):
            self.dllst.insert_at(-10, 'hola')
        # out of the upper bound
        with pytest.raises(ValueError):
            self.dllst.insert_at(99, 'helo')
        # normal
        self.dllst.insert_last(2)
        self.dllst.insert_first('nihao')
        assert self.dllst.get_at(0).data == 'nihao'
        assert self.dllst.get_at(1).data == 'hi'
        assert self.dllst.get_at(2).data == 2
        self.dllst.insert_at(1, 9)
        self.dllst.insert_last('asdf')
        assert self.dllst.get_at(0).data == 'nihao'
        assert self.dllst.get_at(1).data == 9
        assert self.dllst.get_at(2).data == 'hi'
        assert self.dllst.get_at(3).data == 2
        assert self.dllst.get_at(4).data == 'asdf'
        assert self.dllst.get_last().data == 'asdf'
        assert self.dllst.get_at(99) is None

    def test_insert_first(self):
        self.dllst.insert_first(1)
        assert self.dllst.head.data == 1
        self.dllst.insert_first(2)
        assert self.dllst.head.data == 2

    def test_insert_last(self):
        self.dllst.insert_last(1)
        assert self.dllst.get_last().data == 1
        self.dllst.insert_last(2)
        self.dllst.insert_last(3)
        assert self.dllst.get_last().data == 3

    def test_remove_at(self):
        # empty
        try:
            self.dllst.remove_at(4)
        except Exception as e:
            self.fail(e)
        # one
        self.dllst.insert_last(1)
        self.dllst.remove_at(0)
        assert self.dllst.get_at(0) is None
        # multiple
        self.dllst.insert_last(2)
        self.dllst.insert_last(3)
        self.dllst.insert_last(4)
        self.dllst.remove_at(1)
        assert self.dllst.get_at(1).data == 4
        # out of the lower bound -> ignore
        try:
            self.dllst.remove_at(-4)
        except Exception as e:
            self.fail(e)
        assert self.dllst.get_at(1).data == 4
        # out of the upper bound -> ignore
        try:
            self.dllst.remove_at(19)
        except Exception as e:
            self.fail(e)
        assert self.dllst.get_at(1).data == 4

    def test_remove_first(self):
        # empty
        try:
            self.dllst.remove_first()
        except Exception as e:
            self.fail(e)
        # one element
        self.dllst.insert_first(1)
        self.dllst.remove_first()
        assert self.dllst.get_first() is None
        # multiple elements
        self.dllst.insert_first(2)
        self.dllst.insert_first(3)
        self.dllst.insert_first(4)
        assert self.dllst.get_first().data == 4
        self.dllst.remove_first()
        assert self.dllst.get_first().data == 3

    def test_remove_last(self):
        # empty
        try:
            self.dllst.remove_last()
        except Exception as e:
            self.fail(e)
        # one
        self.dllst.insert_first(1)
        self.dllst.remove_last()
        assert self.dllst.get_last() is None
        # multiple
        self.dllst.insert_first(2)
        self.dllst.insert_first(3)
        self.dllst.insert_first(4)
        assert self.dllst.get_last().data == 2
        self.dllst.remove_last()
        assert self.dllst.get_last().data == 3

    def test_every(self):
        self.dllst.insert_last(1)
        self.dllst.insert_last(2)
        self.dllst.insert_last(3)
        self.dllst.insert_last(4)
        try:
            def f(node):
                node.data += 10
            self.dllst.every(f)
        except Exception as e:
            self.fail(e)
        assert self.dllst.get_at(0).data == 11
        assert self.dllst.get_at(1).data == 12
        assert self.dllst.get_at(2).data == 13
        assert self.dllst.get_at(3).data == 14

    def test_iteration(self):
        ''' make it compatible with for-loops & next() function '''
        # empty
        try:
            for node in self.dllst:
                node.data += 10
        except Exception as e:
            self.fail(e)
        assert self.dllst.get_first() is None
        # multiple
        self.dllst.insert_last(1)
        self.dllst.insert_last(2)
        self.dllst.insert_last(3)
        self.dllst.insert_last(4)
        # next() function
        g = iter(self.dllst)
        assert next(g).data == 1
        assert next(g).data == 2
        assert next(g).data == 3
        assert next(g).data == 4
        # for-loop
        try:
            for node in self.dllst:
                node.data += 10
        except Exception as e:
            self.fail(e)
        assert self.dllst.get_at(0).data == 11
        assert self.dllst.get_at(1).data == 12
        assert self.dllst.get_at(2).data == 13
        assert self.dllst.get_at(3).data == 14
