
# Cracking the Coding Interview: Stacks and Queues 3.5
# Problem: Sort a stack such that the smallest items are on the top
# Author: Jordan Tab

# Logic: form a secondary stack that holds values in ascending order

og_stack = [1,56,21,44,7,0,28]

def sort_stack(stack):
    first = stack.pop()
    temp_stack = [28,25,22]

    # order the values in temp_stack largest to smallest
    while len(stack) > 0:
        top = stack[-1]
        temp_top = temp_stack[-1]
        if top < temp_top:
            # pop all numbers that are larger than top
            while top < temp_top:
                top = stack.pop()   
                temp_top = temp_stack.pop()
                stack.append(temp_top)
                if len(temp_stack) == 0:
                    break

        else:
            temp_stack.append(top)
            stack.pop()
    print(temp_stack)

sort_stack(og_stack)
        