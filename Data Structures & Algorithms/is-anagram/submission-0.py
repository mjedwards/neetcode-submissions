class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        loweredS = s.lower()
        loweredT = t.lower()
        for idx, c in enumerate(loweredS):
            if loweredS.count(c) != loweredT.count(c):
                return False
        
        return True