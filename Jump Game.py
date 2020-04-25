class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m = 0
        for i in range(0,len(nums)):
            if(i>m):
                return False
            m = max(m,i+nums[i])
        return True

        
