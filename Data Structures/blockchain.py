import hashlib
import time

def calc_hash(data):
    sha = hashlib.sha256()
    hash_str = data.encode('utf-8')
    sha.update(hash_str)
    return sha.hexdigest()


class Block:
    def __init__(self, data, previous_hash, timestamp=time.time()):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = calc_hash(data+str(timestamp)) #concatinating timestamp to create unique hash
        self.next = None
        
class Blockchain:
    def __init__(self):
        self.head = None
    
    def __str__(self):
        lst = []
        timestamp = []
        node = self.head
        while node:
            lst.append(node.data)
            timestamp.append(int(node.timestamp))
            node = node.next
        if len(lst) == 0:
            return "Data can't be empty"
        return str(lst)
    
    random_hash = hashlib.sha256().hexdigest()
    
    def add_block(self, data, hashed=random_hash):
        if self.head is None:
            self.head = Block(data, self.random_hash)
            if len(self.head.data) == 0:
                raise Exception("Data can't be empty")
            return
        tail = self.head
        while tail.next:
            tail = tail.next
        tail.next = Block(data, tail.hash)
        if len(tail.data) == 0:
            raise Exception("Data can't be empty")
        tail = tail.next
        return
    
    def get_hash(self, data):
        self.data = data
        node = self.head
        while node:
            if node.data == data:
                return node.hash
            node = node.next

    def search_block(self, data):
        self.data = data
        node = self.head
        while node:
            if node.data == data:
                return node
            node = node.next
        return "Node is not presented"

    def remove_block(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        node = self.head
        while node.next:
            if node.next.data == data:
                node.next = node.next.next
                return
            node = node.next
        return "Value is not in the list"



if __name__ == "__main__":

    # Test 1
    print("Test 1")
    blockchain = Blockchain()
    blockchain.add_block("first")
    blockchain.add_block("second")
    blockchain.add_block("third")
    print(blockchain)
    blockchain.remove_block("second")
    blockchain.add_block("fourth")
    print(blockchain)
    print("#"*60)
    # "Test 2 (create different blocks with the same timestamp)"
    print("Test 2 (create different blocks with the same timestamp)")
    blockchain2 = Blockchain()
    blockchain2.add_block("one")
    print(blockchain2.head.timestamp)
    blockchain2.add_block("two")
    print(blockchain2.head.timestamp)
    blockchain2.add_block("three")
    print(blockchain2.head.timestamp)
    print(blockchain2)
    print("#"*60)
   # Test 3 (with empty data)
    print("Test 3 (with empty data)")
    blockchain3 = Blockchain()
    blockchain3.add_block("")
    blockchain3.add_block("")
    print(blockchain3)






