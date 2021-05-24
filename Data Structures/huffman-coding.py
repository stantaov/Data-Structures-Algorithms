import sys
import heapq
import datetime

class HeapNode:
    
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left_node = None
        self.right_node = None
        self.code = ''
    
    def __lt__(self, other):
        return self.freq < other.freq

    def __eq__(self, other):
        if(other == None):
            return False
        if(not isinstance(other, HeapNode)):
            return False
        return self.freq == other.freq

def huffman_encoding(data):
    def frequency(data):
        heapmap = {}
        for char in data:
            count = 1
            if char in heapmap:
                heapmap[char] += count
            else:
                heapmap[char] = count
        #data quality check - can't contain one repeated character, no empty strings allowed
        if len(heapmap) < 2:
            raise  ValueError("Input string can't contain one repeated character or be empty")
        return heapmap
    
    def priority_queue(data):
        priority_queue = []
        frequencies = frequency(data)
        for key, value in frequencies.items():
            node = HeapNode(key, value)
            heapq.heappush(priority_queue, node)
        return priority_queue
    
    priority_queue = priority_queue(data)
    
    def huffman_tree(priority_queue):
        while len(priority_queue) > 1:
            pop1 = heapq.heappop(priority_queue)
            pop2 = heapq.heappop(priority_queue)
            new_node = HeapNode(None, pop1.freq + pop2.freq)
            new_node.left_node = pop1
            new_node.left_node.code = 0
            new_node.right_node = pop2
            new_node.right_node.code = 1
            heapq.heappush(priority_queue, new_node)
        return priority_queue
    
    tree = huffman_tree(priority_queue)
    
    def encoder(tree, val='', ecoder={}):
        bit = val + str(tree.code)
        if tree.left_node:
            encoder(tree.left_node, bit)
        if tree.right_node:
            encoder(tree.right_node, bit)
        if not tree.left_node and not tree.right_node:
            #print(f"{tree.char} -> {bit}")
            ecoder[tree.char] = bit
        return ecoder
    
    ecoder = encoder(tree[0])
    
    def text_encoding(data, ecoder):
        encoder_text = ""
        for i in data:
            if i in ecoder:
                encoder_text += ecoder[i]
        return encoder_text
    
    encoded_text = text_encoding(data, ecoder)
    
    return encoded_text, tree
    
def huffman_decoding(data, tree):
    decoded_string = ''
    current_node = tree
    for current_bit in data:
        if current_bit == '1':
            current_node = current_node.right_node
        if current_bit == '0':
            current_node = current_node.left_node
        if current_node.char is not None:
            decoded_string += current_node.char
            current_node = tree
    return decoded_string

if __name__ == "__main__":
    codes = {}
    # Test 1 (normal sentences)
    print("Test 1 (normal sentences)")
    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree[0])

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    a_great_sentence = "AAAAAAABBBCCCCCCCDDEEEEEE"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree[0])

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    print("#"*60)

    # Test 2 (sentences formed with only one letter)
    a_great_sentence = "AAAAA"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree[0])

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    print("#"*60)
    
    # Test 3 (empty sentences)
    a_great_sentence = ""

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree[0])

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    print("#"*60)
    