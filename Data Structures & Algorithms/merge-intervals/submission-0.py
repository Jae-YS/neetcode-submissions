class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        retVal = []
        cs, ce = intervals[0]
        for i in range(1, len(intervals)):
            ns, ne = intervals[i]
            
            if ns <= ce:
                cs = min(cs, ns)
                ce = max(ce, ne)
            else:
                retVal.append([cs, ce])
                cs, ce = ns, ne
        
        retVal.append([cs, ce])

        return retVal