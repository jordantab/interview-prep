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