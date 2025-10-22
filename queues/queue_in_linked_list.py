class Node:
    def __init__(self, data):
        self.data = data  # dado armazenado no nó
        self.next = None  # referencia para o proximo nó


class Queue:
    def __init__(self):
        self.front = None  # aponta para o o primeiro elemento da fila
        self.rear = None  # aponta para o ultimo elemento da fila
        self.length = 0  # tamanho da fila

    # metodo para adicionar novo elemento na fila
    def enqueue(self, element):
        new_node = Node(element)  # cria um novo nó
        if self.rear is None:  # se a fila estiver vazia
            self.front = self.rear = new_node  # o primeiro e o ultimo no sao o mesmo
            self.length += 1  # adiciona 1 ao tamanho atual da fila
            return
        self.rear.next = new_node  # o ponteiro do ultimo nó apontara para o novo nó criado
        # o ultimo nó recebera o novo nó criado - Passando agora a ser o penultimo nó
        self.rear = new_node
        self.length += 1  # adiciona 1 ao tamanho atual da fila

    # metodo para remover o primeiro da fila
    def dequeue(self):
        if self.isEmpty():  # verifica se a fila esta vazia
            return "Queue is empty"
        temp = self.front  # guarda o primeiro elemento em temp
        self.front = temp.next  # o segundo da fila passa a ser o primeiro
        self.length -= 1  # diminui 1 do tamanho atual da fila
        if self.front is None:  # se o atual primeiro for vazio
            self.rear = None  # o ultimo tbm fica vazio
        return temp.data  # retorna o elemento removido

    # encontra o primeiro da fila
    def peek(self):
        if self.isEmpty():  # se a fila for vazia
            return "Queue is empty"
        return self.front.data  # retorna o data do primeiro no

    def isEmpty(self):
        return self.length == 0

    def size(self):
        return self.length

    # metodo para imprimir a fila
    def printQueue(self):
        temp = self.front  # armazena o primeiro em temp
        while temp:  # enquanto temp for true
            print(temp.data, end=" -> ")  # imprime o data de temp
            temp = temp.next  # pega o proximo no e armazena em temp
        print()  # imprime


# TESTANTO #
myQueue = Queue()

myQueue.enqueue('a')
myQueue.enqueue('b')
myQueue.enqueue('c')

print("Queue: ", end="")
myQueue.printQueue()
print("Peek: ", myQueue.peek())
print("Dequeue: ", myQueue.dequeue())
print("Queue afther Dequeue: ", end="")
myQueue.printQueue()
print("isEmpty: ", myQueue.isEmpty())
print("Size: ", myQueue.size())
