class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        fixed_arr = [0]*26
        for c in s:
            idx = ord(c) - ord('a')
            fixed_arr[idx]+=1
        
        for st in t:
             idx = ord(st) - ord('a')
             fixed_arr[idx]-=1
             if fixed_arr[idx] == -1:
                return False
    
        if sum(fixed_arr) == 0:
            return True
        return False
        # loweredS = s.lower()
        # loweredT = t.lower()
        # for idx, c in enumerate(loweredS):
        #     if loweredS.count(c) != loweredT.count(c):
        #         return False
        
        # return True
        