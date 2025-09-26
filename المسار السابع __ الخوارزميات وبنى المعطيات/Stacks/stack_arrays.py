from sys import maxsize

def create_stack():
    stack = []
    return stack

def is_empty(stack):
    if len(stack) == 0:
        return 'Stack is Empty!'

    return False

def push(stacks, item):
    stacks.append(item)
    print(item , 'pushed to Stack')


def pop(stack):
    if len(stack) == 0:
        return is_empty(stack)

    return f'{stack.pop()} Deleted from Stack'

stack = create_stack()
push(stack, 10)
push(stack, 20)
push(stack, 30)
print(pop(stack))
print(pop(stack))
print(pop(stack))
print(pop(stack))
print(is_empty(stack))