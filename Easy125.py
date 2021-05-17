class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        x = len(s)-1
        y = 0
        while(True):
            while(True):
                print(x,y)
                if ('a'<=s[x] and s[x]<='z') or ('A'<=s[x] and s[x]<='Z') or ( '0'<=s[x] and s[x]<='9'):
                    break
                else:
                    x -= 1
                    if x < 0:
                        return True
            while(True):
                if ('a'<=s[y] and s[y]<='z') or ('A'<=s[y] and s[y]<='Z') or ( '0'<=s[y] and s[y]<='9'):
                    break
                else:
                    y += 1
                    if y > len(s):
                        return True
            if s[x].lower()!=s[y].lower():
                return False
            else:
                x -= 1
                y += 1
                if y >= x:
                    return True