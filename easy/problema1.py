def twoSum(nums: list[int], target: int) -> list[int]:
        retorno = []
        for num in range(len(nums)):
            for i in range(len(nums)):
                if i == num:
                    pass
                elif nums[i] + nums[num] == target:
                    retorno.append(num)
                    retorno.append(i)
                    return retorno