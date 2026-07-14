class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        retval = nums.copy()
        for val in nums:
            retval.append(val)
        
        return retval
    
            
