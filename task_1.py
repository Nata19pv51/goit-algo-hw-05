class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]
        bucket = self.table[key_hash]

        for pair in bucket:
                if pair[0] == key:
                    pair[1] = value
                    return True
                
        bucket.append(key_value)
        return True

    def delete(self, key):
        key_hash = self.hash_function(key)
        bucket = self.table[key_hash]

        for pair in bucket:
            if pair[0] == key:
                bucket.remove(pair)
                return True
        # Якщо цикл завершився і елемент не знайдено, повертаємо False:
        return False


    def get(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

# Тестуємо нашу хеш-таблицю:
H = HashTable(5)
H.insert("apple", 10)
H.insert("orange", 20)
H.insert("banana", 30)

print(H.get("apple"))   # Виведе: 10
print(H.get("orange"))  # Виведе: 20
print(H.get("banana"))  # Виведе: 30

H.delete("orange")
print(H.get("orange"))
