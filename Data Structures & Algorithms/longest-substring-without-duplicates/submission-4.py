class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1

        l, r = 0, 0
        n = len(s)
        substring = ""
        best = 0
        while r < n:
            if s[r] in substring:
                substring=""
                l+=1
                r=l
            
            substring+=s[r]
            best=max(best, len(substring))
            r+=1
        return best
                
              
        