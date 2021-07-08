class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = '{:#b}'.format(n)
        c=0
        for i in a.split("b")[1]:
            if i=='1':
                c+=1
        return c