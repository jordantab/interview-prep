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
    
    def __repr__(self):
        output = f'{self.data}'
        return output

fourth = Node(3)
third = Node(5,fourth)    
second = Node(7,third)
first = Node(5,second)

def print_list(head):
    temp = head

    while (temp):
        print(temp.data, end=" ")
        temp = temp.next
    print()
print_list(first)

def remove_dups(head):
    cur = head
    runner = head.next
    vals = {head.data:1}
    while runner is not None:
        if runner.data in vals:
            cur.next = runner.next
            runner = runner.next
        else:
            vals[runner.data] = 1
            cur = runner
            runner = runner.next
    return head
res = remove_dups(first)
print_list(res)


