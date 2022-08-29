'''
Cracking the Coding Interview: Stacks and Queues 3.2
Problem: Design a stack that returns the minimum element in constant time
Author: Jordan Tab
'''

# Logic: create a hash table that holds the minimum value at each step of the stack. The keys are the numbers in the stack and the value
# pairs are the minimum value at that point


def peak(stack):
    '''returns the top of the stack'''
    return stack[-1]

def pop(stack):
    '''removes the top element from the stack'''
    stack = stack[0:-1]
    return stack

def push(stack,value):
    '''adds an element to the top of the stack'''
    stack.append(value)
    return stack

def min(stack,table):
    '''returns the minimum value of the stack'''
    top = peak(stack)
    return table[top]
stack = [7,2,3,1,5,10]
table = {7:7,2:2,3:2,1:1,5:1,10:1,8:1}
print(peak(stack))
print(pop(stack))
print(push(stack,8))
print(min(stack,table))
pop(stack)