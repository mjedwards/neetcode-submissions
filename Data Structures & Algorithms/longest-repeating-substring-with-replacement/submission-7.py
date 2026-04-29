class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # if len(s) == 0:
        #     return 0
        
        # l, r = 0, 1
        # s_list = [i for i in s]
        # substring = ""

        # while r < len(s_list):
        #     if k > 0 and s_list[l] != s_list[r]:
        #         s_list[r]=s_list[l]
        #         k-=1
        #     elif k == 0 and s_list[l] != s_list[r]:
        #         break
        #     else:
        #         r+=1
                
        
        # return max(len(s[l:r]), len(s[r+1:]))
        count = defaultdict(int)
        l = 0
        best = 0
        max_freq = 0

        for r, ch in enumerate(s):
            count[ch] += 1
            max_freq = max(max_freq, count[ch])

            while (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1

            best = max(best, r - l + 1)

        return best