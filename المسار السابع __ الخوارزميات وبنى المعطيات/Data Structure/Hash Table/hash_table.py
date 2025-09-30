def display_hash(hash_table):
    for i in range(len(hash_table)):
        print(i, end=' ')

        for j in hash_table[i]:
            print('-->', end=' ')
            print(j, end=' ')

        print()

HashTable = [[] for _ in range(10)]

def hashing(key_value):
    return key_value % len(HashTable)


def insert(hash_table, key_value, value):
    hash_key = hashing(key_value)

    hash_table[hash_key].append(value)


insert(HashTable, 10, 'hello')
insert(HashTable, 25, 'mohammed')
insert(HashTable, 20, 'welcome')
insert(HashTable, 9, 'Riyadh')
insert(HashTable, 21, 'Pure')
insert(HashTable, 21, 'Nova')
insert(HashTable, 30, 'Google')

display_hash(HashTable)