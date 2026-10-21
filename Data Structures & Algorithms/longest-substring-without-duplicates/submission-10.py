class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        length = 0
        hs = set()
        l = 0
        r = 0

        while r < len(s):

            if s[r] in hs:
                while s[r] in hs:
                    hs.discard(s[l])
                    l +=1
            
            hs.add(s[r])
            r +=1
            length = max(length, len(hs))
        
        return length
    