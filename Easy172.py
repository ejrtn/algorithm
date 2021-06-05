class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        a = 1
        for i in range(1,n+1):
            a *= i
            
            
        a = str(a)
        print(a)
        c = 0
        for i in range(len(a)-1,-1,-1):
            if a[i] == "0":
                c += 1
            else:
                break
            print(c)
        return c