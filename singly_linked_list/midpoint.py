def midpoint(llst):
    '''find the midpoint node without using size() or a counter variable'''
    if llst.get_first() is None:
        return None

    slow = fast = llst.get_first()
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow
