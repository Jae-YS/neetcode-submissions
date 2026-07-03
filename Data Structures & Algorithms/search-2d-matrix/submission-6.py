class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l, r = 0, len(matrix) - 1
        
        def binarySearch(target, nums: List[int]) -> int:
            l, r = 0, len(nums) - 1

            if target < nums[l]:
                return 2
            elif target > nums[r]:
                return 3
            
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    return 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return 0
        
        while l <= r:
            mid = (l + r) // 2
            print(mid, l, r)
            val = binarySearch(target, matrix[mid])
            if val == 0:
                return False
            elif val == 1:
                return True
            elif val == 2:
                r = mid - 1
            else:
                l = mid + 1  
        return False