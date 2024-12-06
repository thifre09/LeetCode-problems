def isPalindrome(x: int) -> bool:
    x = str(x)
    var1 = x
    var2:str = x[::-1]
    if var1 == var2:
        return True
    else:
        return False
    

def isPalindromeBetter(x: int) -> bool:
    if x < 0:
        return False
    else:
        var1 = x
        var2 = 0
        lenx = 0
        while x != 0:
            x = x // 10
            lenx += 1
        
        x = var1

        for i in range(lenx):
            ultimo_num = x % 10
            x = x // 10
            var2 += ultimo_num * (10 ** (lenx - i-1))
    
        if var1 == var2:
            return True
        else:
            return False

print(isPalindromeBetter(232))