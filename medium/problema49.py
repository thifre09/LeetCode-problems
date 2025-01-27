from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        retorno = []

        for valor in strs:
            util = tuple(sorted(valor))
            if util in hmap.keys():
                l = hmap[util]
                hmap[util] = l
            else:
                hmap[util] = []
            l = hmap[util]
            l.append(valor)
            hmap[util] = l
        
        for v in hmap.values():
            retorno.append(v)
        
        return retorno
    
t = Solution()
print(t.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))