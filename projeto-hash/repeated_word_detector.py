
import string

# classe que representa o hash set


class HashSet:
    def __init__(self, size=100):
        self.size = size
        self.buckets = [[] for _ in range(size)]

# hash function com base na soma dos caracteres e o resto da divisao pelo tamanho da lista
    def hash_function(self, value):
        return sum(ord(char) for char in value) % self.size

# metodo para adicionar elementos ao hash set
    def add(self, value):
        index = self.hash_function(value)  # pega o hash code
        # acha o bucket com base no index / hash code
        bucket = self.buckets[index]
        if value not in bucket:  # verifica se o valor nao existe dentro do bucket
            bucket.append(value)  # adicona se nao existir
            return False  # retorna false se o valor nao existe dentro do bucket
        return True  # retonar true se o valor ja existe no bucket

    def print_set(self):
        # Print all elements in the hash set
        print("Hash Set Contents:")
        for index, bucket in enumerate(self.buckets):
            print(f"Bucket {index}: {bucket}")


texto = """A origem do texto confunde-se com a origem do próprio homem, uma vez que a comunicação entre os seres humanos ocorre por meio de textos. O texto, portanto, nasce no momento em que um homem se comunica com o mundo ou com o outro. Vale a pena ressaltar, não obstante, a origem etimológica de texto: o termo do latim textus, de textum (tecido, entrelaçamento). O texto, portanto, seria o entrelaçamento de signos linguísticos, que, juntos, produzem sentido.
Uma redação escolar escrita de modo desconexo, com partes confusas ou inconclusivas, por exemplo, pode ser considerada um texto mal escrito, haja vista que a tessitura entre as palavras está falhando. Uma boa redação, por outro lado, deve ter coesão e coerência entre as palavras, orações, frases e parágrafos."""

# formatando o texto - tirando letras maiusculas, caracteres especiais e pontuacao
texto = texto.lower()
for pontuacao in string.punctuation + "–”“":
    texto = texto.replace(pontuacao, "")
palavras = texto.split()  # transformando o texto em um array de palavras


hash_set = HashSet(50)  # criando o hash set
repetidas = []  # criando um array vazio para as palavras repetidas

for palavra in palavras:  # percorrendo o array de palavras
    if hash_set.add(palavra):  # adicionando a palavra no hash set e verificando se ela ja existe
        if palavra not in repetidas:  # se existe verificamos de a palavra nao pertence ao array de repetidasd
            # se nao pertence adicionamso ao array repetidas
            repetidas.append(palavra)


print("PALAVRAS REPETIDAS NO TEXTO:")
for palavra in repetidas:
    print(palavra)

print(hash_set.print_set())
