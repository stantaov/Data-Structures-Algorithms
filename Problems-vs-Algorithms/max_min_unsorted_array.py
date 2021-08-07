
import random

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 1:
        return (ints[0], ints[0])
    
    if ints == None:
        return None

    if len(ints) == 0:
        return None

    if ints[0] > ints[1]:
        max_int = ints[0]
        min_int = ints[1]
    else:
        max_int = ints[1]
        min_int = ints[0]
        
    for idx in range(2, len(ints)):
        if ints[idx] > max_int:
            max_int = ints[idx]
        elif ints[idx] < min_int:
            min_int = ints[idx]
    return (min_int, max_int)
            
            

## Example Test Case of Ten Integers

if __name__ == "__main__":
    
    # Test 1 (Null cases)
    print("#"*60)
    print("Test 1 (None and Null cases)")
    l = []
    print ("Pass" if (None == get_min_max(l)) else "Fail")
    # Test 3 (input large list)
    print("#"*60)
    print("Test 3 (input large list)")
    l = [i for i in range(0, 100000)]
    random.shuffle(l)
    print ("Pass" if ((0, 99999) == get_min_max(l)) else "Fail")
    # Test 4 (base cases)
    print("#"*60)
    print("Test 4 (base cases)")
    l = [i for i in range(0, 10)]  # a list containing 0 - 9
    random.shuffle(l)
    print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

