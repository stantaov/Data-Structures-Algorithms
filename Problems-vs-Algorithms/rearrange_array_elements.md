### Problem - Rearrange Array Elements

Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).
for e.g. [1, 2, 3, 4, 5]
The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when there are more than one possible answers, return any one.

### Solution, Time and Space Complexity Analysis

The first step of this algorithm is to sort given data using MergeSort that has O(n log n) time complexity and space complexity o(1). Next, it sorts the list in descending order and after it creates two lists by rearranging each element using the greedy approach to get the max sum. 
