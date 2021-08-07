### Problem - Search in a Rotated Sorted Array

You are given a sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]
You are given a target value to search. If found in the array return its index, otherwise return -1.
You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n).

Example:
Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4

### Solution, Time and Space Complexity Analysis

Using binary search and check whether the left or right split is sorted or not. While doing so I also check if the pivot number is located in either of them. The algorithm continues splitting each sub-list till the pivot equals the middle item or it is not presented in the list. Since I used binary search time complexity is O(log n). Since the while loop is used the space complexity is O(1).