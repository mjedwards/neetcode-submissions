class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t: return s
        
        need = {}

        for c in t:
            need[c] = need.get(c, 0) + 1
        
        have = {}
        l, r = 0, 0
        smallest = ""
        least = len(s)
        formed = 0
        
        while r <= len(s)-1:
            if s[r] in t:
                have[s[r]] = have.get(s[r], 0) + 1
                if have[s[r]] <= need[s[r]]:
                    formed+=1
            
            while formed == len(t):
                if len(s[l:r+1]) <= least:
                    least = len(s[l:r+1])
                    smallest = s[l:r+1] 
                                
                if s[l] in have:
                    have[s[l]]-=1
                    if have[s[l]] < need[s[l]]:
                        formed-=1
                l+=1           
            r+=1

        return smallest
        