class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        
        a = {nums[0]:1}
        r = {nums[0]:1}
       
        for i in range(1,len(nums)):
            c = 0
            for x in a:
                if nums[i]==x:
                    a[x] = a[x]+1
                    c = 1
                    for z in r:
                        if r[z]<a[x]:
                            r = {}
                            r[x] = a[x]
                    break
            if c==0:
                a[nums[i]]=1
        for z in r:
            return z
        