class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        DAG = {}
        for idx, char in enumerate(order):
            DAG[char] = idx
        
        l, r = 0, 1
        print(DAG)

        while r < len(words):
            left = words[l]
            right = words[r]

            word_length = min(len(left), len(right))
            for c1, c2 in zip(left, right):
                if c1 != c2:
                    if DAG[c1] > DAG[c2]:
                        return False
                    break
            else:
            
                if len(left) > len(right):
                    return False
                    
            l = r
            r += 1 

        return True

