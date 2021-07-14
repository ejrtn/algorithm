class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        a = {}
        
        for i in range(len(s)):
            c = 0
            for z in a:
                if s[i]==z:
                    if t[i]!=a[z]:
                        return False
                    c=1
                else:
                    if t[i] == a[z]:
                        return False
            if c==0:
                a[s[i]]=t[i]
        return True
        