from typing import List

class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        counter = 0

        for sub in words:
            if s.startswith(sub):
                counter += 1

        return counter
    
t = Solution()
print(t.countPrefixes(words=["feh","w","w","lwd","c","s","vk","zwlv","n","w","sw","qrd","w","w","mqe","w","w","w","gb","w","qy","xs","br","w","rypg","wh","g","w","w","fh","w","w","sccy"], s="w"))