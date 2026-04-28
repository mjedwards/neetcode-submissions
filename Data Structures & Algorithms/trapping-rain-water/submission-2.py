class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        lmax, rmax = 0, 0
        water = 0

        while l < r:
            if height[l] < height[r]:
                lmax = max(lmax, height[l])
                water += lmax - height[l]
                l += 1
            else:
                rmax = max(rmax, height[r])
                water += rmax - height[r]
                r -= 1

        return water
        # fill = 0
        # l = 0
        # r = len(height) - 1
        # lmax = 0
        # rmax = 0
        # while l < r:
        #     if height[l] >= lmax:
        #         lmax = height[l]
        #     else:
        #         fill+=lmax - height[l]

        #     if height[r] >= rmax:
        #         rmax = height[r]
        #     else:
        #         fill+=rmax - height[r]
                
        #     if lmax <= rmax:
        #         l += 1
        #     else:
        #         r-=1
        # return fill
            