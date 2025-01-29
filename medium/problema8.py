class Solution:
    def myAtoi(self, s: str) -> int:
        retorno = ""
        sinal = None
        passou_sinal = False

        for t in s:
            if t == " ":
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

        if retorno != "":
            retorno = int(retorno)
        else:
            return 0
        
        if sinal == "+":
            return retorno
        elif sinal == "-":
            return -retorno
        else:
            return retorno
        
t = Solution()
print(t.myAtoi("42"))