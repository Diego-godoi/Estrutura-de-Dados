nomes =["diego", "sofia", "maisa", "lucas"] #lista de nomes
print(nomes) ##exibe todos os elementos da lista
print(nomes[0]) ##exibe o elemento de index 0, ou seja o primeiro elemento da lista

##exibindo todos os elementos da lista atravez de um for que percorre a lista toda
for x in nomes:
    print(x) 

#adiciono um novo elemento para o array nomes (o elemento é adicionado no final da lista)
nomes.append("Reginaldo") 
print(nomes)

#remove o elemento da lista correspondente ao index passado
nomes.pop(1)
print(nomes)

#remove o elemento da lista correspondente ao valor passado
nomes.remove("diego")
print(nomes)


# ARRAY METHODS #


nomes.append()#adiciono um novo elemento para o array nomes (o elemento é adicionado no final da lista)
nomes.clear()#remove todos os elemento da lista
nomes.copy() #retorna uma copia da lista
nomes.count() #retorna o numero de elementos da lista com o valor especificado
nomes.extend() #adiciona os elementos de uma lista no final dessa lista
nomes.index() #retorna o index do primeiro elemento com o valor especificado
nomes.insert() #adiona um elemento em uma posicao especificada
nomes.pop() #remove o elemento da lista correspondente ao index passado
nomes.remove() #remove o elemento da lista correspondente ao valor passado
nomes.reverse() #reverte a ordem da lista
nomes.sort() #ordena a lista