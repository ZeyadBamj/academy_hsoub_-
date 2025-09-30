def create_stack():
    stack = []
    return stack

def is_empty(stack):
    if len(stack) == 0:
        return 'Stack is Empty!'

    return False

def push(stack, item):
    stack.append(item)
    print(item , 'pushed to Stack')


def pop(stack):
    if len(stack) == 0:
        return is_empty(stack)

    return f'{stack.pop()} Deleted from Stack'



stacks = create_stack()
push(stacks, 10)
push(stacks, 20)
push(stacks, 30)
# print(pop(stacks))
# print(pop(stacks))
# print(pop(stacks))
# print(pop(stacks))
print(is_empty(stacks))
print(stacks)