class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bs (nums: List) -> bool:
            l, r = 0, len(nums) - 1

            while l <= r:
                mid = (l + r) // 2

                if nums[mid] == target:
                    return True
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1

            return False

        for i in matrix:
            is_found = bs(i)

            if is_found:
                return is_found
        
        return False