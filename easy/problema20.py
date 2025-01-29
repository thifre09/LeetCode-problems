class Solution:
    def isValid(self, s: str) -> bool:
        lista = []

        comeco = ["(", "[", "{"]
        fim = [")", "]", "}"]

        for par in s:
            try:
                if par in comeco:
                    lista.append(par)
                elif par not in comeco:
                    if par == ")" and lista[-1] == "(":
                        del lista[-1]
                    elif par == "]" and lista[-1] == "[":
                        del lista[-1]
                    elif par == "}" and lista[-1] == "{":
                        del lista[-1]
                    else:
                        return False
            except:
                return False
            
        if lista == []:
            return True
        else: 
            return False

t = Solution()
print(t.isValid("(])"))