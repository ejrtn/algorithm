class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        a=[]
        while(True):
            s = 0
            if int(n)==1:
                return True
            elif int(n) in a:
                return False
            
            n=str(n)
            a.append(int(n))
            for r in n:
                s += (int(r)*int(r))
            n=s