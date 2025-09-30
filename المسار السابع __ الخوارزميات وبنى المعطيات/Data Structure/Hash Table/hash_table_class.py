class MyHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]


    def hashing(self, key):
        return key % self.size


    def insert(self, key, value):
        hash_index = self.hashing(key)
        bucket = self.table[hash_index]

        for exists_key in bucket:
            if exists_key == key:
                bucket[hash_index] = [key, value]
                return

        bucket.append([key, value])


    def get(self, key):
        hash_index = self.hashing(key)
        bucket = self.table[hash_index]

        for exists_key, value in bucket:
            if exists_key == key:
                return value

        return 'Key Not Found!'


    def display_hash(self):
        for i in range(len(self.table)):
            print(i, end=' ')

            for j in self.table[i]:
                print('-->', end=' ')
                print(j, end=' ')

            print()


ht = MyHashTable(9)

ht.insert(10, 'apple')
ht.insert(30, 'apple')
ht.insert(24, 'apple')
ht.insert(315, 'apple')
ht.insert(180, 'orange')
ht.insert(270, 'hello')
ht.insert(400, 'what')
ht.insert(120, 'world')
ht.insert(56, 'doing')
ht.insert(360, 'doing')


ht.display_hash()
print(f" Mango: {ht.get(20)}")
