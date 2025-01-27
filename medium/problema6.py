from collections import defaultdict

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = defaultdict(list)
        retorno = ""

        for i in range(numRows):
            rows[i] = []

        n = 0
        estado = True
        
        for letra in s:
            rows[n].append(letra)
            if estado:
                n += 1
            else:
                n -= 1
            
            if n == numRows-1:
                estado = False
            elif n == 0:
                estado = True

        for key in rows.keys():
            retorno += "".join(rows[key])


        return retorno


        
t = Solution()
print(t.convert(s = "PAYPALISHIRING", numRows = 3))