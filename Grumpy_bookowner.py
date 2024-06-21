# 1052. Grumpy Bookstore Owner
# Solved
# Medium
# Topics
# Companies
# Hint
# There is a bookstore owner that has a store open for n minutes. Every minute, some number of customers enter the store. You are given an integer array customers of length n where customers[i] is the number of the customer that enters the store at the start of the ith minute and all those customers leave after the end of that minute.

# On some minutes, the bookstore owner is grumpy. You are given a binary array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.

# When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise, they are satisfied.

# The bookstore owner knows a secret technique to keep themselves not grumpy for minutes consecutive minutes, but can only use it once.

# Return the maximum number of customers that can be satisfied throughout the day.

 

# Example 1:

# Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3
# Output: 16
# Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes. 
# The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.
# Example 2:

# Input: customers = [1], grumpy = [0], minutes = 1






class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """
        n = len(customers)
        
        # Step 1: Calculate initially satisfied customers
        satisfied_customers = 0
        for i in range(n):
            if grumpy[i] == 0:
                satisfied_customers += customers[i]
        
        # Step 2: Calculate the additional satisfied customers with the sliding window
        additional_satisfied = 0
        max_additional_satisfied = 0
        for i in range(n):
            if grumpy[i] == 1:
                additional_satisfied += customers[i]
            
            # Maintain the sliding window of size 'minutes'
            if i >= minutes:
                if grumpy[i - minutes] == 1:
                    additional_satisfied -= customers[i - minutes]
            
            # Update the maximum additional satisfied customers
            max_additional_satisfied = max(max_additional_satisfied, additional_satisfied)
        
        return satisfied_customers + max_additional_satisfied