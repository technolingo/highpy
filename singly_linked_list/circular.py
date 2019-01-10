def is_circular(llst):
    '''checks if a linked list is circular'''
    if llst.head is None or llst.head.next is None:
        return False

    slow = fast = llst.head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
