class MyHashSet:

    def __init__(self):
        self.hash_set = [[] for _ in range(100)]

    def add(self, key: int) -> None:
        func_res = self.hash_function(key)
        for i, el in enumerate(self.hash_set[func_res]):
            if el == key:
                return
        self.hash_set[func_res].append(key)

    def remove(self, key: int) -> None:
        func_res = self.hash_function(key)
        for i, el in enumerate(self.hash_set[func_res]):
            if el == key:
                self.hash_set[func_res][i] = None
                return

    def contains(self, key: int) -> bool:
        func_res = self.hash_function(key)
        for i, el in enumerate(self.hash_set[func_res]):
            if el == key:
                return True
        return False

    def hash_function(self, key: int) -> int:
        return key % 100


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)