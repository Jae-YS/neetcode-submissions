class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False


        find_sum = sum(nums) // k
        sums = [0] * k
        nums.sort(reverse=True)

        def n_subsets(i):
            if i == len(nums): 
                return all(x == find_sum for x in sums)

            for idx in range(k):
                if sums[idx] + nums[i] <= find_sum:
                    sums[idx] += nums[i]
                    if n_subsets(i + 1):
                        return True
                    sums[idx] -= nums[i]
                if sums[idx] == 0:   
                    break

                
            return False
        
        return n_subsets(0)
