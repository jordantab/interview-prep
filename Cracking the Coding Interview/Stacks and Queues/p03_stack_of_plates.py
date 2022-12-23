
# Cracking the Coding Interview: Stacks and Queues 3.3
# Problem: Implement a data structure SetOfStacks that creates a new stack once the previous one exceeds capacity.
# Author: Jordan Tab


threshold = 3

SetofStacks = [[4,3,6],[1,2,8]]

def push(SetofStacks, value):
    last_stack = len(SetofStacks) - 1
    if len(SetofStacks[last_stack]) == threshold:
        SetofStacks.append([value])
    else:
        SetofStacks[last_stack].append(value)
    return SetofStacks

def pop(SetofStacks):
    last_stack = len(SetofStacks) - 1
    SetofStacks[last_stack].pop()

def popAt(SetofStacks, index):
    SetofStacks[index].pop()

print(SetofStacks)
push(SetofStacks,3)
print(SetofStacks)
pop(SetofStacks)
print(SetofStacks)
popAt(SetofStacks,0)
print(SetofStacks)

