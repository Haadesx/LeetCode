# 3171. Find Subarray With Bitwise AND Closest to K
# Solved
# Hard
# Companies
# Hint
# You are given an array nums and an integer k. You need to find a 
# subarray
#  of nums such that the absolute difference between k and the bitwise AND of the subarray elements is as small as possible. In other words, select a subarray nums[l..r] such that |k - (nums[l] AND nums[l + 1] ... AND nums[r])| is minimum.

# Return the minimum possible value of the absolute difference.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,2,4,5], k = 3

# Output: 1

# Explanation:

# The subarray nums[2..3] has AND value 4, which gives the minimum absolute difference |3 - 4| = 1.

# Example 2:

# Input: nums = [1,2,1,2], k = 2

# Output: 0

# Explanation:

# The subarray nums[1..1] has AND value 2, which gives the minimum absolute difference |2 - 2| = 0.

# Example 3:

# Input: nums = [1], k = 10

# Output: 9

# Explanation:

# There is a single subarray with AND value 1, which gives the minimum absolute difference |10 - 1| = 9.

 

# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# 1 <= k <= 109

class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def getandvalue(dictionary, start, end):
            andvalue=0
            for i in range (32):
                if len(dictionary[i])==end-start:
                    andvalue+=2**i
            return andvalue
        closest= float('inf')
        start=0
        end=0
        placevalues={}
        for i in range (32):
            placevalues[i]=set()
        while end<=len(nums):
            relevantval=getandvalue(placevalues ,start, end)
            
            if abs(closest-k)>abs(k-relevantval):
                # print("here1")
                closest=relevantval
            if relevantval > k:
                
                #extend end
                if end == len(nums):
                    break
                addingnum = nums[end]
                counter=0
                while addingnum:
                    
                    if addingnum%2==1:
                        placevalues[counter].add(end)
                    counter+=1
                    addingnum = addingnum//2
                end+=1
            elif relevantval < k:
                
                #shorten start
                for i in range (32):
                    if start in placevalues[i]:
                        placevalues[i].remove(start)
                start+=1
                
            else:
                return 0
            
        return abs(closest-k)
        
                
                
                
                