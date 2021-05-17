class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        result=0
        
        if needle=="" or haystack==needle:
            return 0
        elif (haystack=="" and needle!="") or len(needle)> len(haystack):
            return -1
        else:
            a = []
            for i in range(len(haystack)):
                if needle[0] == haystack[i]:
                    a.append(i)
            
            if len(a)==0:
                return -1
            for i in a:
                c=0
                if len(haystack)-i >= len(needle) :
                    for x in range(len(needle)):
                        if needle[x] == haystack[i+x]:
                            c += 1
                        else:
                            break
                        if len(needle)-1 == x:
                            return i
                else:
                    return -1
            return -1