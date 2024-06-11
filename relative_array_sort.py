# 1122. Relative Sort Array
# Solved
# Easy
# Topics
# Companies
# Hint
# Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

# Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.

 

# Example 1:

# Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# Output: [2,2,2,1,4,3,3,9,6,7,19]
# Example 2:

# Input: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
# Output: [22,28,8,6,17,44]
 

# Constraints:

# 1 <= arr1.length, arr2.length <= 1000
# 0 <= arr1[i], arr2[i] <= 1000
# All the elements of arr2 are distinct.
# Each arr2[i] is in arr1.







class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        # Create a dictionary to store the index of each element in arr2
        index_map = {val: idx for idx, val in enumerate(arr2)}
        
        # Define the custom sorting key
        def custom_sort_key(val):
            if val in index_map:
                return (index_map[val], 0)  # Elements in arr2 come first
            else:
                return (len(arr2), val)  # Elements not in arr2 come later, sorted by value
        
        # Sort arr1 using the custom sorting key
        arr1_sorted = sorted(arr1, key=custom_sort_key)
        
        return arr1_sorted