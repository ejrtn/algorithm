class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        
        
        if len(nums)==0:
            return ""
        
        if len(nums)==1:
            return [str(nums[0])]
        
        a = 0
        r = []
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]+1:
                if a == i-1:
                    r.append(str(nums[i-1]))
                else:
                    r.append(str(nums[a])+"->"+str(nums[i-1]))
                a = i
        if a == len(nums)-1:
            r.append(str(nums[len(nums)-1]))
        else:
            r.append(str(nums[a])+"->"+str(nums[len(nums)-1]))
        return r