class Queue:
    #construtor - cria um objeto com a fila vazia
    def __init__(self):
        self.queue = []
    

    #metodo para adicionar elemento na fila
    def enqueue(self, element):
        self.queue.append(element)

    #metodo para remover o primeiro elemento da fila
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue.pop(0)

    #metodo para retornar o primeiro elemento da fila
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue[0]
    
    #metodo para verificar se a lifa é vazia
    def isEmpty(self):
        return len(self.queue) == 0
    
    #metodo para passar o tamanho da fila
    def size(self):
        return len(self.queue)
    


## TESTANTO ##
myQueue = Queue() #criando objeto

#adicionando elementos
myQueue.enqueue('A')
myQueue.enqueue('b')
myQueue.enqueue('c')

print("Queue: ", myQueue.queue) # retorna a fila inteira
print("Peek: ", myQueue.peek())
print("Dequeue: ", myQueue.dequeue())
print("Queue afther Dequeue: ", myQueue.queue)
print("isEmpty: ", myQueue.isEmpty())
print("Size: ", myQueue.size())