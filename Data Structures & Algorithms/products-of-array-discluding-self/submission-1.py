class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # i = 0
        # prod = 1
        # res = []
        # while i < len(nums):
        #     ignore = i
        #     for j in range(len(nums)):
        #         if j != ignore:
        #             prod*=nums[j]
        #     res.append(prod)
        #     prod = 1
        #     i+=1
        
        # return res
        n = len(nums)
        res = [1] * n

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
            
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res
        