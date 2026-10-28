class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        r = len(nums) - 1
        count = 0

        for idx, num in enumerate(nums):
            if num == val:
                while r > -1 and nums[r] == val:
                    r -= 1
                nums[idx] = nums[r]
                r -= 1
            else:
                count += 1
        return count
        