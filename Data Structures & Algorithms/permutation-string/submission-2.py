class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        L = len(s1)
        if L > len(s2):
            return False

        def idx(c: str) -> int:
            return ord(c) - ord('a')

        need = [0] * 26
        window = [0] * 26

        for c in s1:
            need[idx(c)] += 1

        # initial window
        for c in s2[:L]:
            window[idx(c)] += 1

        if window == need:
            return True

        # slide window
        for r in range(L, len(s2)):
            window[idx(s2[r])] += 1
            window[idx(s2[r - L])] -= 1
            if window == need:
                return True

        return False
        # l, r = 0, 0
        # formed = 0
        # L = len(s1)

        # while formed != L:
        #     if s2[r] in s1:
        #         formed+=1
            
        #     while formed == L:
        #         if s2[l] in s1:
        #             break
        #         l+=1
        #     r+=1

        # a = [i for i in s2[l:r]]
        # a.sort()
        # b = ''.join([i for i in a])
        # return s1 == b
        

        
