class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        newnums=[]
        ctr=0
        for i in nums:
            if(i!=0):
                newnums.append(i)
                ctr += 1       
        for i in range(0,len(nums)-ctr):
            newnums.append(0)  
        for i in range(0,len(nums)):
            nums[i]=newnums[i]
             
