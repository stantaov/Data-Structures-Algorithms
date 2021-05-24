class LRU_Cache:
    def __init__(self, capacity):
        self.cache = {}
        self.slots = []
        self.capacity = capacity
        
    def get(self, key):
        if key in self.slots:
            value = self.cache[key]
            idx = self.slots.index(value)
            self.slots.pop(idx)
            self.slots.insert(0, value)
            return self.slots
        else:
            return -1

    def set(self, key, value):
        if self.capacity == 0:
            return "LRU capacity should be > 0"
        if self.capacity < 0:
            return "LRU capacity can't be < 1"
        if self.capacity > 5:
            return "LRU slots can't be more than 5"
        if len(self.slots) == self.capacity:
            self.slots.pop(-1)
            self.slots.insert(0, value)
            return self.cache, self.slots
        else:   
            self.cache[key] = value
            self.slots = list(self.cache.values())
            self.slots.reverse()
        return self.cache, self.slots

# Test 1 (provided by Udacity)
print("Test 1 (provided by Udacity)")
our_cache = LRU_Cache(5)

print(our_cache.set(1, 1));
print(our_cache.set(2, 2));
print(our_cache.set(3, 3));
print(our_cache.set(4, 4));


print(our_cache.get(1))      # returns 1
print(our_cache.get(2))      # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

print(our_cache.set(5, 5)) 
print(our_cache.set(6, 6))

our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
print("#"*60)

# Test 2 (when capacity is 0 should return "LRU capacity should be > 0")
print("Test 2 (when capacity is 0 should return 'LRU capacity should be > 0')")
our_cache = LRU_Cache(0)
print(our_cache.set(1, 1))
assert our_cache.set(1, 1) == "LRU capacity should be > 0"
print("#"*60)
# Test 3 (when capacity is negative should return "LRU capacity can't be < 1")
print("Test 3 (when capacity is negative should return 'LRU capacity can't be < 1')")
our_cache = LRU_Cache(-1)
print(our_cache.set(1, 1))
assert our_cache.set(1, 1) == "LRU capacity can't be < 1"
print("#"*60)
# Test 4 (when capacity is exciding allowed slots should return "LRU slots can't be more than 5")
print("Test 4 (when capacity is exciding allowed slots should return 'LRU slots can't be more than 5')")
our_cache = LRU_Cache(10)
print(our_cache.set(1, 1))
assert our_cache.set(1, 1) == "LRU slots can't be more than 5"
print("#"*60)


