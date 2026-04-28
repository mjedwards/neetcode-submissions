class Solution:
    def trap(self, height: List[int]) -> int:
        fill = 0
        l = 0
        r = len(height) - 1
        lmax = 0
        rmax = 0
        while l < r:
            if height[l] >= lmax:
                lmax = height[l]
            else:
                fill+=lmax - height[l]

            if height[r] >= rmax:
                rmax = height[r]
            else:
                fill+=rmax - height[r]
                
            if lmax <= rmax:
                l += 1
            else:
                r-=1
        return fill
            