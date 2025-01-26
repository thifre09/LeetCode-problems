from typing import List

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        lista = []
        repetidos = []
        for n in nums:
            if n in lista:
                repetidos.append(n)
            else:
                lista.append(n)
        for item in repetidos:
            lista = [i for i in lista if i != item]

        return sum(lista)
    
teste = Solution()

print(teste.sumOfUnique([-2,-1,1,1,1,1,1]))