class Solution(object):
    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """
        def canPlaceBalls(min_force):
            count = 1
            last_pos = position[0]
            
            for i in range(1, len(position)):
                if position[i] - last_pos >= min_force:
                    count += 1
                    last_pos = position[i]
                    if count == m:
                        return True
            return False
        
        position.sort()
        low, high = 1, position[-1] - position[0]
        
        while low <= high:
            mid = (low + high) // 2
            if canPlaceBalls(mid):
                low = mid + 1
            else:
                high = mid - 1
        
        return high