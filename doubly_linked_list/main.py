class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def clear(self):
        self.head = None

    def size(self):
        counter = 0
        node = self.head
        while node:
            counter += 1
            node = node.next
        return counter

    def get_at(self, index):
        if index < 0 or not self.head:
            return None
        counter = 0
        node = self.head
        while node:
            if index == counter:
                return node
            counter += 1
            node = node.next
        return None

    def get_first(self):
        return self.get_at(0)

    def get_last(self):
        node = self.head
        while node:
            if node.next is None:
                return node
            node = node.next
        return None

    def insert_first(self, data):
        new_node = Node(data, None, self.head)
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def insert_at(self, index, data):
        if index < 0:
            raise ValueError('Invalid index')
        elif index == 0:
            self.insert_first(data)
        else:
            prev_node = self.get_at(index - 1)
            if prev_node is None:
                raise ValueError('Invalid index')
            new_node = Node(data, prev_node, prev_node.next)
            if prev_node.next is not None:
                prev_node.next.prev = new_node
            prev_node.next = new_node

    def insert_last(self, data):
        last = self.get_last()
        if last is not None:
            last.next = Node(data, last)
        else:
            self.head = Node(data)

    def remove_first(self):
        if self.head is None:
            return
        if self.head.next is not None:
            self.head.next.prev = None
        self.head = self.head.next

    def remove_at(self, index):
        if index < 0 or self.head is None:
            return  # out of lower bound
        elif index == 0:
            self.remove_first()
        else:
            prev_node = self.get_at(index - 1)
            if prev_node is None or prev_node.next is None:
                return  # out of upper bound

            if prev_node.next.next is not None:
                prev_node.next.next.prev = prev_node

            prev_node.next = prev_node.next.next

    def remove_last(self):
        node = self.head
        if node is None:
            return
        elif node.next is None:
            self.head = None
            return
        while node:
            if node.next.next is None:
                node.next = None
                return
            node = node.next

    def every(self, func):
        ''' apply func to every node, return nothing'''
        node = self.head
        while node:
            func(node)
            node = node.next

    def __repr__(self):
        head = self.head.data
        size = self.size()
        return f'A LinkedList with head data {head} & length {size}.'

    def __len__(self):
        return self.size()

    def __iter__(self):
        ''' make it compatible with for-loops '''
        self.node = self.head
        return self

    def __next__(self):
        ''' make it compatible with next() function '''
        if self.node is None:
            raise StopIteration
        current = self.node
        self.node = self.node.next
        return current
