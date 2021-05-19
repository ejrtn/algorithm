class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        a = {}
        c=0
        for i in nums:
            c=0
            for x in a:
                if x==i:
                    a[i] += 1
                    c=1
                    break
            if c!=1:
                a[i] = 1
        print(a)
        for i in a:
            if a[i]==1:
                return i