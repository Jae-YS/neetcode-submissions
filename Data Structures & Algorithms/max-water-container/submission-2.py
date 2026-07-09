class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        max_amount = 0

        while l < r:
            height = min(heights[l], heights[r])
            diff = height * (r - l)
            max_amount = max(max_amount, diff)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return max_amount
