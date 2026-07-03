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
            for i in range(word_length):
                if left[i] != right[i]:
                    if DAG[left[i]] > DAG[right[i]]:
                        return False
                    else:
                        break
                if i == word_length - 1 and len(left) > len(right):
                    return False
            l = r
            r += 1 

        return True

