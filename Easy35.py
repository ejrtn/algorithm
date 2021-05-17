class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        r = 0
        s = None
        for i in range(len(nums)):
            if nums[i] == target:
                s = i
                break
            elif nums[i] > target:
                r = i
                break;
            elif i==len(nums)-1:
                r = i+1
            
        if s is not None:
            return s
        else:
            return r
            