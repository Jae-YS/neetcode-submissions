class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        total = 0
        hl, hr = 0, 0

        while left <= right:
            if height[left] <= height[right]:
                hl = max(hl, height[left])
                total += hl - height[left]
                left += 1
            else:
                hr = max(hr, height[right])
                total += hr - height[right]
                right -= 1

        return total

