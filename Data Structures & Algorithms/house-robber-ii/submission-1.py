class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]


        nums1 = nums[1:]
        nums2 = nums[:-1]
        dp1 = [0] * len(nums1)
        dp1[0] = nums1[0]
        for i in range(1, len(nums1)):
            if i == 1:
                dp1[i] = max(dp1[0], nums1[1])
            else:
                dp1[i] = max(dp1[i - 1], dp1[i - 2] + nums1[i])
        
        dp2 = [0] * len(nums2)
        dp2[0] = nums2[0]
        for i in range(1, len(nums2)):
            if i == 1:
                dp2[i] = max(dp2[0], nums2[1])
            else:
                dp2[i] = max(dp2[i - 1], dp2[i - 2] + nums2[i])
        
        



        return max(max(dp1), max(dp2))