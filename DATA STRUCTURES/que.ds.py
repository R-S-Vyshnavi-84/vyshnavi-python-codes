from queue import LifoQueue
stack=LifoQueue(maxsize=3)
print(stack.qsize())
stack.put('a')
stack.put('b')
stack.put('c')

print("Full: ", stack.full())
print("Size: ", stack.qsize())
print("\nelements popped from the stack")
print(stack.get())
print(stack.get())
print(stack.get())