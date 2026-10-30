class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        retVal = []
        ns, ne = newInterval


        for curr_start, curr_end in intervals:
            if ns <= curr_end and ne >= curr_start:
                ns = min(ns, curr_start)
                ne = max(ne, curr_end)
            elif curr_end < ns:
                retVal.append([curr_start, curr_end])
            else:
                retVal.append([ns, ne])
                ns, ne = curr_start, curr_end
        
        retVal.append([ns, ne])

        return retVal