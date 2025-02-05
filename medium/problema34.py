from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]

        low1 = 0
        high1 = len(nums)-1
        mid = low1 + (high1-low1)//2

        while nums[mid] != target:
            mid = low1 + (high1-low1)//2

            if nums[mid] == target:
                elemento1 = mid
            elif nums[mid] < target:
                low1 = mid + 1
            elif nums[mid] > target:
                high1 = mid - 1
        
        # binary search na esquerda

        low2 = low1
        high2 = mid

        while True:
            mid2 = low2 + (high2-low2)//2

            if nums[low2] == target:
                menor = low2
                break
            elif nums[mid2] < target:
                low1 = mid2 + 1
            elif nums[mid2] > target:
                high1 = mid2 - 1
            else:
                low2 += 1

        # binary search na direita

        low2 = mid
        high2 = high1

        while True:
            mid2 = low2 + (high2-low2)//2

            if nums[high2] == target:
                maior = high2
                break
            elif nums[mid2] < target:
                low1 = mid2 + 1
            elif nums[mid2] > target:
                high1 = mid2 - 1
            else:
                high2 -= 1

        return [menor, maior]
    
t = Solution()
print(t.searchRange(nums = [1,2,2,2,2,3,4,5,5,5,5,6,7,8,9,10,11,12,12,12,12,12,13], target = 12))