'''
Cracking the Coding Interview: Linked Lists 2.5
Problem: You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order.
Write a function that adds the two numbers and returns the sum as a linked list
    Example:
        7->1->6 + 5->9->2 = 617 + 295 = 2->1->9 = 912
Author: Jordan Tab
'''




def sum_lists(list1,list2):
    '''
    adds together two linked lists that represent integers

    logic: each digit is a multiple of a power of 10. convert the linked lists into an int, get the digits of the total and reverse them
    to create new linked list
    '''
    n1 = 0
    n2 = 0
    cur1 = list1
    cur2 = list2
    x = 0
    while cur1 is not None:
        n1 += cur1.data * (10**x)
        cur1 = cur1.next
        x += 1
    y = 0
    while cur2 is not None:
        n2 += cur2.data * (10**x)
        cur2 = cur2.next
        y += 1
    total = n1 + n2
    total = str(total)
    rev = total[::-1]
    last = list1
    for i in len(rev):
        if i == 0:
            last = Node(rev[i],rev[i+1])
        elif == len(rev):
            Node(rev[i],None)
        else:
            Node(rev[i],rev[i+1])
    return last