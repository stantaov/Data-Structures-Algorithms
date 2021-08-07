def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) == 0 or input_list == [None]:
        return [-1,-1]

    input_list = mergeSort(input_list)
    result = [0,0]
    is_right = False
    for i in input_list:
        i = str(i)
        if is_right:
            result[1] = int(str(result[1]) + i)
            is_right = False
        else:
            result[0] = int(str(result[0]) + i)
            is_right = True
    return result
    
def mergeSort(arr):
    
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = mergeSort(left)
    right = mergeSort(right)
    return merge(left, right)

def merge(a, b):
    result = []
    
    while a and len(a) > 0 and b and len(b) > 0:
        if a[0] > b[0]:
            result.append(a.pop(0))
        else:
            result.append(b.pop(0))
    while a and len(a) > 0:
        result.append(a.pop(0))
    while b and len(b) > 0:
        result.append(b.pop(0))
    return result
    
def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

if __name__ == "__main__":


    print(mergeSort([10,3,1,4,5,6,4,3,2,3,4,5,5,6]))
    
    # Test 1 (None and Null cases)
    print("#"*60)
    print("Test 1 (None and Null cases)")
    test_function([[], [-1,-1]])
    test_function([[None],[-1,-1]])
    # Test 2 (input list has only one element)
    print("#"*60)
    print("Test 2 (input list has only one element)")
    test_function([[1],[1,0]])
    # Test 3 (long input list)
    print("#"*60)
    print("Test 3 (long input list)")
    test_function([[10,3,1,4,5,6,4,3,2,3,4,5,5,6], [10654432, 6554331]])
    test_function([[4,5,5,4,3,3,6,6,7,8,6,4,3,3,2,3,4], [866544332, 76544333]])
    # Test 4 (base cases)
    print("#"*60)
    print("Test 4 (base cases)")
    test_function([[1, 2, 3, 4, 5], [542, 31]])
    test_function ([[4, 6, 2, 5, 9, 8], [964, 852]])
    test_function([[9, 2,5,6,0,4], [952, 640]])
