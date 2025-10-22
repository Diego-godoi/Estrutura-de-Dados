class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    # metodo para adicionar novo elemento
    def push(self, value):
        new_node = Node(value)  # cria um novo no
        if self.head:  # se existir um head
            # o no criado passa a ser o head ou seja referencia o none pq ele é o ultimo da pilha
            new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        popped_node = self.head  # armazeno o ultimo elemento em popped_node
        # pego o proximo elemento depois do head e passo para o head, ou seja o proximo elemento depois do head passa a ser o novo head
        self.head = self.head.next
        self.size -= 1
        return popped_node.value

    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.head.value

    def isEmpty(self):
        return self.size == 0

    def stackSize(self):
        return self.size

    def traverseAndPrint(self):
        currentNode = self.head  # armazena o head em currentNode
        while currentNode:  # enquando currentNode exisitr
            # imprimir o valor de current node
            print(currentNode.value, end=" - > ")
            # current node passar a ser o proximo elemento da pilha
            currentNode = currentNode.next
        print()


# TESTANDO #
myStack = Stack()
myStack.push('A')
myStack.push('B')
myStack.push('C')

print("LinkedList: ", end="")
myStack.traverseAndPrint()
print("Peek: ", myStack.peek())
print("Pop: ", myStack.pop())
print("LinkedList after Pop: ", end="")
myStack.traverseAndPrint()
print("isEmpty: ", myStack.isEmpty())
print("Size: ", myStack.stackSize())
