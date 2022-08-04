'''
Cracking the Coding Interview: Linked Lists 2.2
Problem: Implement an algorithm to find the kth to last element of a singly linked list
Author: Jordan Tab
'''

class Node:
    '''
    Node class
    '''
    def __init__(self,data,next=None):
        '''
        constructor
        '''
        self.data = data
        self.next = next
    
    def __repr__(self):
        output = f'{self.data}'
        return output

sixth = Node(3)        
fifth = Node(1,sixth)
fourth = Node(8,fifth)
third = Node(2,fourth)    
second = Node(7,third)
first = Node(5,second)

def kth_to_last(head,k):
    '''
    returns kth to last element in a singly linked list

    logic: have two pointers, one pointing to the first node the other k elements ahead of the first one. When the ahead pointer reaches the
    end, the slower pointer will be k nodes behind
    '''
    cur = head
    run = head
    for i in range(k):
        run = run.next
    while run.next is not None:
        cur = cur.next
        run = run.next
    return cur
print(kth_to_last(first,3)) # 2