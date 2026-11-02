class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        idx = 0
        total = -1
        if sum(gas) < sum(cost):
            return -1
        for i in range(len(gas)):
            if total < 0:
                print("here", i)
                idx = i
                total = gas[i] - cost[i]
            else:
                total = total - cost[i] + gas[i]
            


        return idx