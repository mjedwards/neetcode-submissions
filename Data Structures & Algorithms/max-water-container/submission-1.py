class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        best = 0
        while l < r:
            if heights[l] < heights[r]:
                best = max(best, heights[l]*len(heights[l:r]))
                l+=1
            elif heights[r] < heights[l]:
                best = max(best, heights[r]*len(heights[l:r]))
                r-=1
            elif heights[r] == heights[l]:
                best = max(best, heights[l]*len(heights[l:r]))
                l+=1
        return best
        