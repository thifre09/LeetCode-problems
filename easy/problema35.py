from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        mid = low + (high-low)//2

        while high >= low:

            mid = low + (high-low)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid+1
            elif nums[mid] > target:
                high = mid-1

        if high < 0 or low < 0:
            return 0

        return low
            
t = Solution()
print(t.searchInsert(nums = [1,2,3], target = 4))