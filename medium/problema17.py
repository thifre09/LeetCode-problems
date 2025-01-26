from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keyboard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        retorno = []

        i = 0

        for i,digit in enumerate(digits):
            for j, digit2 in enumerate(digits):
                valor = keyboard[digit[i]]
                valor += keyboard[digit2[j]]
                retorno.append(valor)


teste = Solution()
teste.letterCombinations("23")
            
