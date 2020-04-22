class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sdict = {0:1}
        n = len(nums)
        count = 0
        s = 0
        for i in nums:
            s += i
            if s-k in sdict:
                count += sdict[s-k]
            if s in sdict:
                sdict[s] += 1
            else:
                sdict[s] = 1
        return count
