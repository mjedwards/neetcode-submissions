class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        best = 0
        curr_len = 1
        current = 0
        for x in nums_set:
            if x - 1 not in nums_set:
                current = x
            
                while current+1 in nums_set:
                    curr_len+=1
                    current+=1
            
            best = max(best, curr_len)
            curr_len = 1
        return best

        