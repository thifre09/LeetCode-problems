class Solution:
    def myAtoi(self, s: str) -> int:
        retorno = ""
        sinal = None
        passou_sinal = False

        for t in s:
            if t == " " and passou_sinal == False:
                continue
            elif t == "+" and passou_sinal == False:
                sinal = "+"
                passou_sinal = True
            elif t == "-" and passou_sinal == False:
                sinal = "-"
                passou_sinal = True
            elif t.isnumeric():
                retorno += t
                passou_sinal = True
            else:
                break

        if retorno != "" and sinal is not None:
            retorno = sinal + retorno
            retorno = int(retorno)
        elif retorno != "":
            retorno = int(retorno)
        else:
            return 0
        
        if retorno >= 2**31-1:
            return 2**31-1
        elif retorno <= -(2**31):
            return -(2**31)
        
        return retorno
        
t = Solution()
print(t.myAtoi("42"))