queue = []

#adicionando - novos elemento ficam no final da fila
queue.append('A')
queue.append('B')
queue.append('C')
print("Queue: ", queue)

#retorna o primeiro elemento
frontElement = queue[0]
print("Peek: ", frontElement)

#removendo elemento
poppedElement = queue.pop(0)
print("Dequeue: ", poppedElement)

print("Queue afther dequeue: ", queue) #primeiro da fila removido

#verificando se é vazio
isEmpty = not bool(queue)
print("isEmpty: ", isEmpty)

#Tamanho
print("Size: ", len(queue))