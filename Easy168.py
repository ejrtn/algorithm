class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        
        a = ['A','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','O','R','S','T','U','V','W','X','Y','Z']
        
        r = ""
        C=0
        while(True):
            print(columnNumber)
            if columnNumber%26==0:
                c = 26
                columnNumber -= 1
            else:
                c = columnNumber%26
            if columnNumber<27:
                r = a[c]+r
                return r
            r = a[c]+r
            columnNumber /= 26
            