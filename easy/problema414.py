from typing import List

def thirdMax(nums: List[int]) -> int:
    maximo = max(nums)
    for num in nums:
        if num == maximo:
            nums.remove(num)

    maximo = max(nums)
    for num in nums:
        if num == maximo:
            nums.remove(num)

    maximo = max(nums)
    return maximo
    



print(thirdMax(nums = [3,2,1]))