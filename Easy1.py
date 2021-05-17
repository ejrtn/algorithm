class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a=[]
        for i in range(len(nums)):
            for x in range(i+1,len(nums)):
                if (nums[i]+nums[x])==target:
                    a.append(i)
                    a.append(x)
                    return a