class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = [int(x) for x in str(num)]
        for i, val in enumerate(digits):
            if val == 9:
                continue
            cur_max = val
            idx = i
            for j in range(len(digits) -1, i, -1):
                if digits[j] > cur_max:
                    cur_max = digits[j]
                    idx = j
            
            if cur_max != val:
                digits[idx] = val
                digits[i] = cur_max
                return int("".join(map(str, digits)))

        return int("".join(map(str, digits)))

