def isPalindrome(x: int) -> bool:
    x = str(x)
    var1 = x
    var2:str = x[::-1]
    if var1 == var2:
        return True
    else:
        return False
    

print(isPalindrome(-5555555555555555555555553444444444334444444443555555555555555555555555))
