class HashTable:
    def __init__(self):
        self.collection = {}
        
    def hash(self, char=''):
        return sum(ord(ch) for ch in char)
    def add(self, key, value):
        hashed_key = self.hash(key)
        self.collection[hashed_key] = value
    def remove(self, key):
        hashed_key = self.hash(key)
        if hashed_key in self.collection:
            bucket = self.collection[hashed_key]
            for i, (k,v) in enumerate(bucket):
                if k == key:
                    del bucket[i]
            return         

    def lookup(self, key):
        pass             