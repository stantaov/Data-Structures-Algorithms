def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    if input_list == None:
        return None
    if input_list == []:
        return []
    if len(input_list) == 1:
        return input_list
    low = 0
    high = len(input_list)-1
    i = 0
    while(i <= high):
        if(input_list[i] == 0):
            input_list[i], input_list[low] = input_list[low], input_list[i]
            i += 1
            low += 1
        elif(input_list[i] == 2):
            input_list[i], input_list[high] = input_list[high], input_list[i]
            high -= 1
        else:
            i += 1
    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    if sorted_array == None:
        print(sorted_array)
        print("Pass")
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

if __name__ == "__main__":
    
    # Test 1 (None and Null cases)
    print("#"*60)
    print("Test 1 (None and Null cases)")
    test_function([])
    test_function([None])
    # Test 2 (input list has only one element)
    print("#"*60)
    print("Test 2 (input list has only one element)")
    test_function([0])
    test_function([1])
    test_function([2])
    # Test 3 (input list has two elemnts)
    print("#"*60)
    print("Test 3 (input list has two elemnts)")
    test_function([1, 0])
    test_function([1, 1])
    test_function([2, 2])
    test_function([2, 1])
    # Test 4 (base cases)
    print("#"*60)
    print("Test 4 (base cases)")
    test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
    test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
    test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

