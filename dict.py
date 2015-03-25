class Set:
    def __init__(self):
        self.store = {}
    def insert(self, el):
        self.store[el] = True
        return True
    def delete(self, el):
        del self.store[el]
        return True
    def intersection(self, other_set):
        result = Set()
        items = self.store.keys()
        for item in items:
            if other_set.present(item):
                result.insert(item)
        return result
    def present(self, key):
        return key in self.store
    def union(self, other_set):
        result = Set()
        items = self.store.keys()
        for item in items:
            result.insert(item)
        items = other_set.store.keys()
        for item in items:
            result.insert(item)
        return result

s1 = Set()
s1.insert("hello")
s1.insert("world")
s2 = Set()
s2.insert("world")
s2.insert("domination")
print(s1.intersection(s2).store)
print(s2.intersection(s1).store)
print(s1.union(s2).store)
print(s2.union(s1).store)
s1.delete("world")
print(s1.intersection(s2).store)
print(s1.union(s2).store)
