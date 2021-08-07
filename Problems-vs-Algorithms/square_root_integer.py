
def sqrt(number):
    """
    This function calculates the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    start = 0 
    end = number

    if number == 0 or number == 1:
        return number

    if number == None:
        return None

    if number < 0:
        return -1 

    while start <= end:
        mid = (start + end) // 2

        if mid * mid == number:
            return mid

        elif mid * mid <= number:
            start = mid + 1
            square_root = mid
        else:
            end = mid - 1

    return square_root


if __name__ == "__main__":
    
    # Test 1 (number = None)
    print("#"*60)
    print("Test 1 (input number is None)")
    print ("Pass" if (None == sqrt(None)) else "Fail")
    print("#"*60)
    # Test 2 (number is negative integer)
    print("Test 2 (input number is negative integer)")
    print ("Pass" if  (-1 == sqrt(-128)) else "Fail")
    print("#"*60)
    # Test 3 (number is null)
    print("Test 3 (input number is null)")
    print ("Pass" if  (0 == sqrt(0)) else "Fail")
    print("#"*60)
    # Test 4 (base cases)
    print("Test 4 (base cases)")
    print ("Pass" if  (4 == sqrt(16)) else "Fail")
    print ("Pass" if  (1 == sqrt(1)) else "Fail")
    print ("Pass" if  (5 == sqrt(27)) else "Fail")
    print ("Pass" if  (3 == sqrt(9)) else "Fail")
    print("#"*60)
    # Test 5 (large number test)
    print("Test 4 (input number is large number)")
    print ("Pass" if  (10000 == sqrt(100000000)) else "Fail")
    print("#"*60)