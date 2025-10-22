class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        popped_node = self.head
        self.head = self.head.next
        self.size -= 1
        return popped_node.value

    def isEmpty(self):
        return self.size == 0

    def stackSize(self):
        return self.size

    def traverseAndPrint(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.value, end=" -> ")
            currentNode = currentNode.next
        print()


# testando #
print("PALINDROME CHECKER")
word = input("Digite uma palavra: ").lower().replace(" ", "")
stack = Stack()
invertedWord = ""

for x in word:
    stack.push(x)

while not stack.isEmpty():
    invertedWord += stack.pop()

if word == invertedWord:
    print("This is a palindrome")
    print("Word: ", word)
    print("Inverted Word: ", invertedWord)
else:
    print("This is not palindrome")
    print("Word: ", word)
    print("Inverted Word: ", invertedWord)
