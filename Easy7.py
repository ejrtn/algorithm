class Solution(object):
    def reverse(self, x):
        x = str(x)
        """
        :type x: int
        :rtype: int
        """
        if int(x) == -2^31 or int(x) == 2^31-1 or int(x)==0:
            return 0
        elif int(x)>0:
            a=""
            for i in range(len(x)-1,-1,-1):
                a+=x[i]
            if int(a)<=2**31-1:
                return int(a)
            else:
                return 0
        else:
            a="-"
            for i in range(len(x)-1,0,-1):
                a+=x[i]
            if int(a)>=-2**31:
                return int(a)
            else:
                return 0