def takeCharacters(s: str, k: int) -> int:
    direita = len(s)-1
    esquerda = 0

    nums = {
        "a": 0,
        "b": 0,
        "c": 0
    }

    for digito in s:
        if digito == "a":
            nums["a"] += 1
        elif digito == "b":
            nums["b"] += 1
        elif digito == "c":
            nums["c"] += 1
        if nums["a"] and nums["b"] and nums["c"] >= k:
            break
    
    for value in nums:
        if nums[value] < k:
            return -1
        else:
            continue
    
    

            
        
print(takeCharacters("aaaabbbcc",2))