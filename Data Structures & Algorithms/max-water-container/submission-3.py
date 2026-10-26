class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        total = 0
        while l < r:
            curr_height = min(heights[l], heights[r]) 
            area = curr_height * (r - l)
            total = max(area, total)                       
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return total
