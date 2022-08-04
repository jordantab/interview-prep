'''
Cracking the Coding Interview: Linked Lists 2.1
Problem: Remove duplicates from an unsorted linked list
Author: Jordan Tab
'''
# create a linked list
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
    
first = Node(4)
