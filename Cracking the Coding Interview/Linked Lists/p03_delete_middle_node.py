'''
Cracking the Coding Interview: Linked Lists 2.2
Problem: Implement an algorithm to delete a node in the middle (any node but the first and last node, not necessarily the exact middle) of
a singly linked list, given only access to that node
    Example:
        list = a -> b -> c -> d -> e
        delete c
        output = a -> b -> d -> e
Author: Jordan Tab
'''

from calendar import c
from pytest import PytestUnhandledThreadExceptionWarning


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

# create test nodes
fifth = Node('e')
fourth = Node('d',fifth)
third = Node('c',fourth)    
second = Node('b',third)
first = Node('a',second)

# function to print the linked list
def print_list(head):
    temp = head

    while (temp):
        print(temp.data, end=" ")
        temp = temp.next
    print()
print_list(first)

def delete_middle_node(head,node):
    '''
    deletes the given node from the linked list

    logic: only have access to the current node, update it with the contents of the next node and delete the next node since we can't
    access the previous node
    '''
    temp = head
    while temp.data != node:
        temp = temp.next
    if temp.data == node:
        temp.data = temp.next.data
        temp.next = temp.next.next
    return head
    
res = delete_middle_node(first,'c')
print_list(res)