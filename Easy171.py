class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        

        r = 0
        c = len(columnTitle)-1
        z = 0
        while(True):
            if c == -1:
                break
            r += ((26**c)*(ord(columnTitle[z])-64))
            c -= 1
            z += 1
            # print(r)
        return r
        