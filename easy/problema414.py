from typing import List

def thirdMax(nums: List[int]) -> int:
    nums = set(nums)
    nums = list(nums)
    
    if len(nums) == 1:
        return nums[0]
    
    elif len(nums) == 2:
        maximo = max(nums)
        return maximo
    

    elif len(nums) >= 3:
        index = 0
        maximo = max(nums)
        for num in nums:
            if num == maximo:
                nums.remove(num)
                nums.insert(index, False)
            index += 1

        nums_filtrado = []
        for obj in nums:
            if not (obj is False):
                nums_filtrado.append(obj)
        
        index = 0
        maximo = max(nums_filtrado)
        for num in nums_filtrado:
            if num == maximo:
                nums_filtrado.remove(num)
                nums_filtrado.insert(index, False)
            index += 1

        nums_filtrado2 = []
        for obj in nums_filtrado:
            if not (obj is False):
                nums_filtrado2.append(obj)


        maximo = max(nums_filtrado2)
        return maximo
    



print(thirdMax(nums = [-4,-5,-3,-2,-1]))