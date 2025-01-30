from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = 0

        low = 0
        high = len(nums)-1
        mid = low + (high-low)//2

        while mid != high and mid != low:

            mid = low + (high-low)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid+1
            elif nums[mid] > target:
                high = mid-1

        if high < 0 or low < 0:
            return 0 
        
        if len(nums) == 1:
            if nums[0] > target:
                return 0 
            elif nums[0] < target:
                return 1
            else:
                return 0

        if mid < low:
            return low
        elif mid > high:
            return high
            
t = Solution()
print(t.searchInsert(nums = [1], target = 1))