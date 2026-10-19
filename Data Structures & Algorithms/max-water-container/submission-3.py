class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        vol = 0

        while l < r:
            curVol = (r - l) * min(heights[l], heights[r])

            if curVol > vol:
                vol = curVol
            
            if heights[l] > heights[r]:
                r -= 1
                continue
            elif heights[r] > heights[l]:
                l += 1
                continue

            l += 1
            
        return vol
            




        