class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        freq = Counter(hand)
        if len(hand) % groupSize != 0:
            return False
        for _ in range(len(hand) // groupSize):
            s = min(freq.keys())            
            for i in range(s, s + groupSize): 
                if i not in freq:
                    return False
                else:
                    freq[i] -= 1
                    if freq[i] == 0:
                        del freq[i]
                i += 1
            





        
        return True