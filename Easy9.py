class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        if int(x)>=0:
            a=""
            for i in range(len(x)-1,-1,-1):
                a+=x[i]
            if a==x:
                return True
            else:
                return False
        else:
            return False