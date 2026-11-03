class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        freq = Counter(hand)
        minH = list(freq.keys())
        heapq.heapify(minH)
        while minH:
            first = minH[0]
            for i in range(first, first + groupSize):
                if i not in freq:
                    return False
                freq[i] -=1
                if freq[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True