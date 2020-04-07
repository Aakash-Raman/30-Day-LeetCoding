class Solution:
    def countElements(self, arr: List[int]) -> int:
        ctr = 0
        for i in arr:
            if(i+1 in arr):
                ctr += 1
        return ctr        
