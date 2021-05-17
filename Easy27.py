class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        size = len(nums)
        c = 0
        while(True):
            if len(nums)-1 == c or len(nums)==0:
                if len(nums)==0:
                    break
                if nums[c] == val:
                    del nums[c]
                break
            else:
                if nums[c] == val:
                    del nums[c]
                else:
                    c += 1