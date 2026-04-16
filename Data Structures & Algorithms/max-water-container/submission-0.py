class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        l, r = 0, len(heights)-1

        while l < r:
            area = 0
            if heights[l] < heights[r]:
                area = (r-l)*heights[l]
                l+=1
            else:
                area = (r-l)*heights[r]
                r-=1
            max_water = max(max_water, area)
        return max_water

