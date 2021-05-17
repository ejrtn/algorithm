class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        min=len(strs[0])
        for i in range(1,len(strs)):
            if min > len(strs[i]):
                min = len(strs[i])
        if min == 0:
            return ""
        result=""
        x=0
        c=0
        while(True):
            if len(strs)==1:
                result=strs[0]
                break
            for i in range(1,len(strs)):
                if strs[0][x] != strs[i][x]:
                    c=1
                    break
                elif i==len(strs)-1:
                    result+=strs[0][x]
            x+=1
            if c==1:
                break
            if x==min:
                break
        return result