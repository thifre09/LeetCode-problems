from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        setnums = list(set(nums))
        lennums = len(nums)
        lensetnums = len(setnums)
        nums = list(set(nums))
        for i in range((lennums-lensetnums)):
            nums.append("_")
        print(nums)
        return lensetnums

teste = Solution()

print(teste.removeDuplicates(nums = [1,1,2]))

