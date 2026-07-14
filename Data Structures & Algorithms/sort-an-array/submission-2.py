class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        l, r = 0, 0
        retval = []
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                retval.append(left[l])
                l += 1
            else:
                retval.append(right[r])
                r += 1
            
        while l < len(left):
            retval.append(left[l])
            l += 1
        while r < len(right):
            retval.append(right[r])
            r += 1
        return retval
            


        