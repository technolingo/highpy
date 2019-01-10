def get_nth_node_from_last(llst, n):
    '''find the n-th node counting from the tail in a linked list,
       assuming n is smaller or equal to the length of the linked list.
    '''
    if llst.head is None or n < 0:
        return None
    elif n == 0:
        return llst.head

    slow = fast = llst.head

    for _ in range(n):
        fast = fast.next

    while n > 0:
        if fast.next is None:
            return slow
        slow = slow.next
        fast = fast.next
