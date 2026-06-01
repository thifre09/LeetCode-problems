class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        str1 = list(ransomNote)
        str2 = list(magazine)
        for letter in str1:
            if letter in str2:
                str2.remove(letter)
            else:
                return False
        return True