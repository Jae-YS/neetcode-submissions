class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        fors = [1]

        for i in range(len(nums) - 1):
            val = fors[i] * nums[i]
            fors.append(val)

        prev = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            fors[i] *= prev
            prev *= nums[i]

            


        return fors