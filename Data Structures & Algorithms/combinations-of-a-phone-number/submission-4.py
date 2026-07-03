class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        combo = [] 
        
        num_to_char = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t" ,"u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        
        def go_through(idx, s):
            
            if idx == len(digits):
                combo.append("".join(s))
                return
                
            digit = digits[idx]

            for char in num_to_char[digit]:
                s.append(char)
                go_through(idx + 1, s)
                s.pop()
            

        go_through(0, []) 

        return list(combo)