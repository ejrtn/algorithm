class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        
        a = ""
        z = n
        while(True):
            a = str(z%2)+a
            z /= 2
            if z == 0:
                
                for i in range(32-len(a)):
                    a = "0"+a
                break
        n = a
        r = 0
        for i in range(len(n)-1,-1,-1):
            if n[i]=="1":
                r += (2**i)
            print(i)
        return r