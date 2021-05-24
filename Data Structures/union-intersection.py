class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next
        return size
            
            
    def to_list(self):
        lst = []
        node = self.head
        while node:
            lst.append(node.value)
            node = node.next
        return lst
    
def union(llist_1, llist_2):
    lst1 = llist_1.to_list() 
    lst2 = llist_2.to_list()
    if  len(lst1) == 0 and len(lst2) == 0:
        return "Both lists are empty!"
    else:    
        combined = lst1 + lst2 
        union = []
        for item in combined: 
            if item not in union: 
                union.append(item)
        return union

def intersection(llist_1, llist_2):
    lst1 = llist_1.to_list() 
    lst2 = llist_2.to_list()
    if  len(lst1) == 0 and len(lst2) == 0:
        return "Both lists are empty!"
    else: 
        intersection = []
        for item in lst1: 
            if item in lst2 and item not in intersection: 
                intersection.append(item)
        return intersection

if __name__ == "__main__":

    # Test case 1 (normal)
    print("Test case 1 (normal)")
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,21]
    element_2 = [6,32,4,9,6,1,11,21,1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)
    print("Union")
    print (union(linked_list_1,linked_list_2))
    print("Intersection")
    print (intersection(linked_list_1,linked_list_2))
    assert union(linked_list_1,linked_list_2) == [3, 2, 4, 35, 6, 65, 21, 32, 9, 1, 11]
    assert intersection(linked_list_1,linked_list_2) == [4, 6, 21]
    print("#"*60)
    # Test case 2 (one list is empty)
    print("Test case 2 (one list is empty)")
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = []
    element_2 = [1,7,8,9,11,21,1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)
    print("Union")
    print (union(linked_list_3,linked_list_4))
    print("Intersection")
    print (intersection(linked_list_3,linked_list_4))
    assert union(linked_list_3,linked_list_4) == [1, 7, 8, 9, 11, 21]
    assert intersection(linked_list_3,linked_list_4) == []
    print("#"*60)

    # Test case 3 (both list are empty)
    print("Test case 3 (both list are empty)")
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = []
    element_2 = []

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)
    print("Union")
    print (union(linked_list_3,linked_list_4))
    print("Intersection")
    print (intersection(linked_list_3,linked_list_4))
    assert union(linked_list_3,linked_list_4) == "Both lists are empty!"
    assert intersection(linked_list_3,linked_list_4) == "Both lists are empty!"
    print("#"*60)