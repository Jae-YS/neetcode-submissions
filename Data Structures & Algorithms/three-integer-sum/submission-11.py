class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums) 
        idx = 0
        retVal = []
        for idx in range(len(nums) - 2 ):
            if idx > 0 and nums[idx] == nums[idx - 1]:
               continue

            left, right = idx + 1, len(nums) - 1
            while left < right:
                total = nums[idx] + nums[left] + nums[right]
                if total == 0:
                    retVal.append([nums[idx], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -=1 
                        
                elif total > 0:
                    right -= 1
                else:
                    left += 1
        return retVal
                
