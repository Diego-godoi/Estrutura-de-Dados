stack = ['b','c','d']

stack.append('a')
stack.append(2)
print("Stack: ", stack)

topElement = stack[-1]
print("Peek: ",topElement)

poppedElement = stack.pop()
print("Pop: ", poppedElement)

print("Stack afther Pop: ", stack)

isEmpty = not bool(stack)
print("isEmpty: ",isEmpty)

print("Size: ",len(stack))