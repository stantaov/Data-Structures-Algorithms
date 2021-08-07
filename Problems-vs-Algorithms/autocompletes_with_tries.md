### Solution, Time and Space Complexity Analysis

The main data structure of any trie is a map(dictionary) since it allows to create nested data structures that can be optimally used in the tree-like structure to store strings. The time complexity is directly related to the length of the target word n and the number of words in the trie N -> O(n*N) -> O(n).

Trie -> the time complexity of the insert method is O(n) since the algorithm needs to iterate through the target word and space complexity is O(n) since it needs to store all values of the target word.

Trie -> the time complexity of the find method is O(n) since the algorithm needs to iterate through the target word and space complexity is O(1) only one value is needed to be stored

TrieNode -> the time complexity of the suffixes method is O(n) since it needs to iterate through each node and space complexity is O(1) only one value is needed to be stored



