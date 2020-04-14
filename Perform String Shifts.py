class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        m = 0
        length = len(s)
        for direction,amount in shift:
            if direction == 0:
                m = m+amount
            else:
                m = m-amount
        m = m%length
        return s[m:]+s[:m]
            
        # abc
