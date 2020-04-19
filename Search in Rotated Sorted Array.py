class Solution:
    def search(self, nums: List[int], target: int) -> int:
        flag = 0
        for i in range(0,len(nums)):
            if(target == nums[i]):
                return i
                flag = 1
        if(flag == 0):
            return -1
