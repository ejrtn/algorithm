class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        
        z = ""
        for i in range(len(s)-1,-1,-1):
            if s[i] != " ":
                for x in range(i,-1,-1):
                    if s[x] == " ":
                        return len(z)
                    z += s[x]
                print(z)
                return len(z)
        
        return len(z)