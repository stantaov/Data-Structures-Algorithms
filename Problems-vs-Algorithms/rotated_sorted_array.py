
def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """

    if len(input_list) <= 0 or number == None or input_list == None:
        return - 1
    

    start=0
    end=len(input_list)-1
    mid = 0
    while start<=end:
        mid=(start+end)//2
        if input_list[mid]==number:
            return mid
        if input_list[mid]>=input_list[0]: # check if left range is sorted
            if input_list[mid]<number or input_list[0]>number: # check if the number is not within the left ragne
                start=mid+1 # increase left range
            else:
                end=mid-1 # decrease left range
        else: # if left range is not sorted than right range should be sorted
            if input_list[mid]>number or input_list[-1]<number: # check if the number is not within the right ragne
                end=mid-1 # increase right range
            else:
                start=mid+1 # decrease right range
    return -1 
        
    

def linear_search(input_list, number):
    if len(input_list) <= 0 or number == None or input_list == None:
        return - 1
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


if __name__ == "__main__":

    # Test 1 (None cases)
    print("#"*60)
    print("Test 1 (input_list, and input number are None or empty)")
    test_function([[None], None])
    test_function([[], None])
    test_function([[], 1])
    test_function([[], []])
    test_function([[1,2,3], None])
    print("#"*60)
    # Test 2 (input list has only one element)
    print("Test 2 (input list has only one element)")
    test_function([[5], 1])
    test_function([[5], 7])
    print("#"*60)
    # Test 3 (input list has two elements)
    print("Test 3 (input list has two elements)")
    test_function([[1,2], 1])
    test_function([[1,2], 7])
    print("#"*60)
    # Test 4 (base cases)
    print("Test 4 (base cases)")
    test_function([[9, 10, 1, 2, 3, 4, 5, 6, 7, 8], 3])
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 8])
    test_function([[6, 7, 8, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 10])
    print("#"*60)

