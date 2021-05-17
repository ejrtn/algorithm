class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        sum=0
        i=0
        while(True):
            if len(s)==1:
                return arr[s[i]]
            if arr[s[i]] < arr[s[i+1]]:
                sum+=(arr[s[i+1]]-arr[s[i]])
                i+=2
            else:
                sum+=arr[s[i]]
                i+=1
            if i>=len(s):
                return sum
            if i==len(s)-1:
                sum+=arr[s[i]]
                return sum