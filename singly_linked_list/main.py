class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    ''' A singly linked list.'''

    def __init__(self, head=None):
        self.head = head

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

    def insert_at(self, index, data):
        if index <= 0 or self.head is None:
            self.head = Node(data, self.head)
            return

        counter = 0
        node = self.head
        while node:
            if counter == index - 1:
                next_node = None
                if node.next:
                    next_node = node.next
                node.next = Node(data, next_node)
                return
            elif node.next is None:
                # out of the upper bound
                node.next = Node(data)
                return
            counter += 1
            node = node.next

    def insert_first(self, data):
        self.insert_at(0, data)

    def insert_last(self, data):
        last = self.get_last()
        if last:
            last.next = Node(data)
        else:
            self.head = Node(data)

    def remove_at(self, index):
        if index < 0 or self.head is None:
            return
        elif index == 0:
            self.head = self.head.next
            return

        counter = 0
        node = self.head
        while node:
            if counter == index - 1:
                next_node = None
                if node.next:
                    if node.next.next:
                        next_node = node.next.next
                # replacing the target with its subsequent node
                node.next = next_node
                return
            counter += 1
            node = node.next

    def remove_first(self):
        self.remove_at(0)

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
