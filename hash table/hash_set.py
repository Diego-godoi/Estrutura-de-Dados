class SimpleHashSet:
    # construtor para o hash set
    def __init__(self, size=100):
        self.size = size  # define o tamho
        # cria a quantidade de bucket de acordo com o tamanho
        self.buckets = [[] for _ in range(size)]

    def hash_function(self, value):
        # retorna o hash code / index de acordo com o resultado do modulo
        return sum(ord(char) for char in value) % self.size

    def add(self, value):
        # pega o index com base no hash function
        index = self.hash_function(value)
        bucket = self.buckets[index]  # pega o bucket com base no index passado
        if value not in bucket:  # se o valor nao pertencer ao bucket entao ele nao exite e adicionamos o valor
            bucket.append(value)

    def contains(self, value):
        index = self.hash_function(value)
        bucket = self.buckets[index]
        return value in bucket  # retorna se o valor pertence ao bucket

    def remove(self, value):
        index = self.hash_function(value)
        bucket = self.buckets[index]
        if value in bucket:
            bucket.remove(value)  # se o valor pertencer ao bucket entao remova

    def print_set(self):
        print("Hash Set Contents: ")
        for index, bucket in enumerate(self.buckets):
            print(f"bucket {index}: {bucket}")


# Creating the Hash Set from the simulation
hash_set = SimpleHashSet(size=10)

hash_set.add("Charlotte")
hash_set.add("Thomas")
hash_set.add("Jens")
hash_set.add("Peter")
hash_set.add("Lisa")
hash_set.add("Adele")
hash_set.add("Michaela")
hash_set.add("Bob")

hash_set.print_set()

print("\n'Peter' is in the set:", hash_set.contains('Peter'))
print("Removing 'Peter'")
hash_set.remove('Peter')
print("'Peter' is in the set:", hash_set.contains('Peter'))
print("'Adele' has hash code:", hash_set.hash_function('Adele'))
