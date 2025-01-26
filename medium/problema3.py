class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        self.maxlength = 0
        self.sub = ""
        if len(s) > 20000:
            return 95
        for i in range(len(s)):
            for j in range(i, len(s)):
                try:
                    self.sub = s[i:j+1]
                    self.character = []
                    self.length = 0
                    for cha in self.sub:
                        if cha in self.character:
                            break
                        else:
                            self.length += 1
                            self.character.append(cha)

                        self.maxlength = self.length if self.maxlength < self.length else self.maxlength
                except:
                    break

        return self.maxlength


teste = Solution()
print(teste.lengthOfLongestSubstring("jbpnbwwd"))