class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def is_pali(w):
            l, r = 0, len(w) - 1
            while l <= r:
                if w[l] != w[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        def backtrack(idx, curr, cache):
            if idx == len(s):
                res.append(curr[:])
                return
            for i in range(idx, len(s)):
                substr = s[idx:i + 1]
                check = False
                if substr not in cache:
                    check = is_pali(substr)
                    cache[substr] = check
                else:
                    check = cache[substr]

                if check:
                    curr.append(substr)
                    backtrack(i + 1, curr, cache)
                    curr.pop()
    
        backtrack(0, [], {})
        return res 


        
            
        
        
