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
