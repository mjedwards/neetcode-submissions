class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            middle = (left + right) // 2

            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle

        return nums[left]
        # while len(nums) > 1:
        #     middle = len(nums) // 2

        #     if nums[middle] > nums[-1]:
        #         nums = nums[middle + 1:]

        #     elif nums[middle] < nums[-1]:
        #         nums = nums[:middle + 1]

        # return nums[0]
        
