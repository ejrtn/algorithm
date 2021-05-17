class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        i=0
        count=0
        s=len(nums)
        if s==0:
            return 0
        if s==1:
            return 1
        while(True):
            if nums[i]==nums[i+1]:
                del nums[i]
                s -= 1
            else:
                i += 1
            if s-1==i:
                break
            
        return s