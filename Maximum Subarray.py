class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s=nums[0]
        newlist=[]
        newlist.append(s)
        for i in range(1,len(nums)):
            if(nums[i]>nums[i]+s):
                newlist.append(nums[i])
                s=nums[i]
            else:
                newlist.append(nums[i]+s)
                s=nums[i]+s
        newlist.sort()
        print(newlist)
        return newlist[len(newlist)-1]
