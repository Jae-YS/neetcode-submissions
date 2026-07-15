import math

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        loops = math.gcd(len(nums), k)
        visited = set()
        i = 0
        temp = 0
        l, r = 0, k
        val = nums[0]
        while i < loops:
            temp = nums[r]
            nums[r] = val
            val = temp
            l = r
            r = (r + k) % len(nums)
            if r in visited:
                seen = set()
                i += 1
                if i == loops:
                    break
                l, r = i, i + k
                val = nums[l]                
            else:
                visited.add(r)
        return
            
                


